# Data format

`catalog.json` lists 33 main tasks and five paired noise settings. The `id` and
`panel` pair identifies one released input. The scientific `task_id` inside a
packet is preserved from the evaluated input and may differ from the catalog ID.

Each discovery packet contains `task.json` and `observations.npz`. The task
document describes the measured or simulated fields, units, geometry, known
conditions, observation records and modeling purpose. Scientific descriptions
and array files are copied unchanged from the current experimental selection.

NPZ files contain NumPy arrays and load with `allow_pickle=False`. Array names,
shapes and dtypes for every file are recorded in `data_manifest.json`.

| Representation | Main arrays |
|---|---|
| Regular scalar or coupled fields | `time` (or `t`), spatial coordinates, named fields |
| Most regular fields | `[record, time, spatial axes...]` |
| Annular mesh | `nodes`, `triangles`, `boundary_tags`, `time`, `u[record,time,node]` |
| PIV velocities | `u[time,n,s,channel]`, `t`, `n`, `s`, `valid`; channels described in task |
| Cell profiles | `u[record,time,x]`, `time` in days, `x` in mm |
| Surface elevations | `u[record,time,x]`, `time` in seconds, `x` in metres |

Do not infer axis order from a filename: read the task's `observations`,
`data_axes`, `field_axes`, field declarations and manifest. Some tasks provide
additional observed fields connected by known kinematic relations.

The separate conditions packet contains `query.json` and the relevant arrays:
`conditions.npz`, or `initial_conditions.npz` and `boundary_controls.npz`.
For some smooth synthetic tasks, `known_conditions.json` specifies continuous
preparation/control functions sampled by these arrays. These are known inputs,
not the unknown evolution law. Measured tasks use sampled initial fields and
edge histories; no unmeasured continuous preparation is invented.

`load_conditions` returns the query document and a dictionary of arrays grouped
by filename. Use it after fixing the equation and numerical coefficients.

Checksums bind the exact released inputs. Author-source reconstructions also
check each array's shape, dtype and value bytes, so a NumPy ZIP-container encoding
change is distinguished from a change in the scientific data.
