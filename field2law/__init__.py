"""Load Field2Law's released observations and separately supplied conditions."""
from pathlib import Path
import hashlib
import json
import shutil
import numpy as np

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def catalog(root=DEFAULT_ROOT):
    return json.loads((Path(root)/'catalog.json').read_text())


def task_record(task_id, panel='main', root=DEFAULT_ROOT):
    matches=[t for t in catalog(root)['tasks'] if t['id']==task_id and t['panel']==panel]
    if len(matches)!=1:
        raise ValueError(f'Unknown task: {panel}/{task_id}')
    return matches[0]


def arrays(path):
    with np.load(path, allow_pickle=False) as z:
        return {k:z[k] for k in z.files}


def load_task(task_id, panel='main', root=DEFAULT_ROOT):
    """Return the unchanged scientific task document and public arrays."""
    record=task_record(task_id,panel,root)
    folder=Path(root)/record['public_path']
    if not (folder/'observations.npz').exists():
        raise FileNotFoundError(f"Run: python -m field2law fetch-external {record['external_source']}")
    return json.loads((folder/'task.json').read_text()),arrays(folder/'observations.npz')


def load_conditions(task_id, panel='main', root=DEFAULT_ROOT):
    """Load known forecast inputs after the discovered model is fixed."""
    folder=Path(root)/task_record(task_id,panel,root)['conditions_path']
    doc=json.loads((folder/'query.json').read_text())
    manifest=json.loads((Path(root)/'data_manifest.json').read_text())['files']
    expected=[
        Path(root)/p for p in manifest if (Path(root)/p).parent==folder and p.endswith('.npz')]
    missing=[p.name for p in expected if not p.exists()]
    if missing:
        raise FileNotFoundError('Acquire the author-source data first: '+', '.join(missing))
    known=folder/'known_conditions.json'
    if known.exists():doc['continuous_conditions']=json.loads(known.read_text())
    return doc,{p.name:arrays(p) for p in expected}


def verify(root=DEFAULT_ROOT, require_external=False):
    root=Path(root);manifest=json.loads((root/'data_manifest.json').read_text())['files']
    checked=0;external_missing=[];errors=[];array_equivalent=[]
    for name,spec in manifest.items():
        p=root/name
        if not p.exists():
            (external_missing if not spec['included'] else errors).append(name)
            continue
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if digest!=spec['sha256']:
            # NPZ container encoding may differ across NumPy versions; the
            # reconstructed author's individual arrays must remain exact.
            if spec['included'] or p.suffix!='.npz':
                errors.append(name);continue
            a=arrays(p)
            same=set(a)==set(spec['arrays']) and all(
                list(a[k].shape)==v['shape'] and str(a[k].dtype)==v['dtype']
                and hashlib.sha256(np.ascontiguousarray(a[k]).tobytes()).hexdigest()==v['sha256']
                for k,v in spec['arrays'].items())
            if not same:errors.append(name);continue
            array_equivalent.append(name)
        checked+=1
    return dict(ok=not errors and (not require_external or not external_missing),
                checked=checked,external_arrays_not_acquired=external_missing,
                array_equivalent_containers=array_equivalent,errors=errors)


def export_task(task_id, destination, panel='main', conditions=False, root=DEFAULT_ROOT):
    """Export a single task, without catalog labels or other tasks."""
    record=task_record(task_id,panel,root)
    source=Path(root)/record['conditions_path' if conditions else 'public_path']
    if conditions:load_conditions(task_id,panel,root)
    else:load_task(task_id,panel,root)
    destination=Path(destination)
    if destination.exists():raise FileExistsError(destination)
    shutil.copytree(source,destination)
    return destination
