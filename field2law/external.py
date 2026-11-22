"""Acquire fixed author-source files and reproduce the measured input packets."""
from pathlib import Path
import _codecs
import hashlib
import io
import json
import pickle
import urllib.request
import numpy as np
from . import DEFAULT_ROOT, task_record, verify

SOURCES={
 'pc3':dict(task='measured_cells_loading',
   url='https://raw.githubusercontent.com/jlager/BINNs/41d4b8f3e06597449f76750cf840d2bee7111143/Data/cell_density_profiles.npy',
   sha256='0b6af8ea30f39809795a33c0bc28a60a07ccbc70f6f0f13515a24b1e635d5ab9'),
 'waves':dict(task='measured_wave_window',
   url='https://raw.githubusercontent.com/Scientific-Artificial-Intelligence-Lab/kd/b691ec950ce235cae37a2fa669cd39f425c5f1ad/src/kd/_assets/data/wave_breaking_N_G2Tp12A100_broad.npz',
   sha256='e070f58f656d27f589494e11753920fce4b43771961a11ecf367dda5e7a5deb9'),
}


class ArrayUnpickler(pickle.Unpickler):
    def find_class(self,module,name):
        from numpy.core.multiarray import _reconstruct
        allowed={('numpy.core.multiarray','_reconstruct'):_reconstruct,
                 ('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype,
                 ('_codecs','encode'):_codecs.encode}
        if (module,name) not in allowed:raise ValueError('Unexpected object in author data')
        return allowed[module,name]


def acquire(source, local_file=None, root=DEFAULT_ROOT):
    info=SOURCES[source];root=Path(root)
    if local_file is not None:payload=Path(local_file).read_bytes()
    else:
        request=urllib.request.Request(info['url'],headers={'User-Agent':'Field2Law-data-loader'})
        with urllib.request.urlopen(request,timeout=120) as response:payload=response.read()
    if hashlib.sha256(payload).hexdigest()!=info['sha256']:
        raise ValueError('Author-source checksum mismatch; no data written')
    record=task_record(info['task'],root=root)
    public=root/record['public_path'];conditions=root/record['conditions_path']
    task=json.loads((public/'task.json').read_text());query=json.loads((conditions/'query.json').read_text())
    if source=='pc3':
        f=io.BytesIO(payload);version=np.lib.format.read_magic(f)
        if version==(1,0):np.lib.format.read_array_header_1_0(f)
        elif version==(2,0):np.lib.format.read_array_header_2_0(f)
        else:raise ValueError('Unexpected NPY format')
        data=ArrayUnpickler(f).load().item()
        def select(records):
            return np.stack([data[f"dens_{r['initial_cells_per_well']}"][f"U{r['replicate']}"][1:,:].T*1000
                             for r in records])
        ref=data['dens_10000'];x=ref['x'][1:,0]/1000;time=ref['t'][:,0]/24
        observed=select(task['records']);held=select(query['records'])
        pub_arrays=dict(x=x,time=time,u=observed)
        cond_arrays=dict(x=x,time=time,initial=held[:,0],boundary=held[:,:,[0,-1]])
    else:
        with np.load(io.BytesIO(payload),allow_pickle=False) as z:t,x,eta=(z[k] for k in ['t','x','eta'])
        time,frames=np.unique(t,return_inverse=True)
        first=np.sort(x[frames==0]);gaps=np.flatnonzero(np.diff(first)>20*np.median(np.diff(first)))
        if len(gaps)!=2:raise ValueError('Unexpected camera layout')
        separators=(first[gaps]+first[gaps+1])/2;component=np.searchsorted(separators,x)
        bounds=[(x[(frames==j)&(component==1)].min(),x[(frames==j)&(component==1)].max()) for j in range(39)]
        grid=np.linspace(max(v[0] for v in bounds)+.01,min(v[1] for v in bounds)-.01,129)
        sampled=[]
        for j in range(len(time)):
            ids=np.flatnonzero((frames==j)&(component==1));ids=ids[np.argsort(x[ids])]
            if x[ids[0]]>grid[0] or x[ids[-1]]<grid[-1]:raise ValueError('Missing spatial coverage')
            sampled.append(np.interp(grid,x[ids],eta[ids]))
        u=np.asarray(sampled);future=np.arange(39,len(time));width=5
        pub_arrays=dict(time=time[:39],x=grid,u=u[None,:39])
        cond_arrays=dict(time=time[future],x=grid,initial__u=u[None,39],
                         boundary_strips=np.stack([u[future,:width],u[future,-width:]],axis=1)[None])
    # Source files contain evaluation measurements as well. Only the declared
    # discovery arrays and known forecast conditions are persisted here.
    destinations={public/'observations.npz':pub_arrays,conditions/'conditions.npz':cond_arrays}
    manifest=json.loads((root/'data_manifest.json').read_text())['files']
    for path,values in destinations.items():
        wanted=manifest[str(path.relative_to(root))]['arrays']
        assert set(values)==set(wanted)
        for k,v in values.items():
            assert list(v.shape)==wanted[k]['shape'] and str(v.dtype)==wanted[k]['dtype']
            assert hashlib.sha256(np.ascontiguousarray(v).tobytes()).hexdigest()==wanted[k]['sha256'],k
    for path,values in destinations.items():np.savez_compressed(path,**values)
    return dict(source=source,source_sha256=info['sha256'],arrays_match_registered_data=True,
                written=[str(p.relative_to(root)) for p in destinations],hidden_future_arrays_written=False)
