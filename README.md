# Field2Law

**Benchmarking PDE Discovery from Expert Workflows to Autonomous Agents**

Field2Law studies how methods turn field observations and physical context into
interpretable evolution laws that remain useful under new conditions. It covers
synthetic physical applications and experimental measurements, connecting PDE
discovery to the practical task of building a reusable model.

This repository provides the **public data and task preview**: 33 main tasks
(28 synthetic, 5 measured) and 5 paired observation-noise controls. External
expert review has been arranged; reviewed revisions will be recorded explicitly.
The manuscript is in preparation.

## Start here

```bash
git clone https://github.com/JunchengZhong/Field2Law-Bench.git
cd Field2Law-Bench
python -m pip install -e .
python -m field2law list
python -m field2law verify
python -m field2law inspect physical_001
```

PIV excerpts are included under their source license. Cell-migration and
surface-wave arrays are reconstructed from fixed author-source files:

```bash
python -m field2law fetch-external pc3
python -m field2law fetch-external waves
python -m field2law verify --require-external
```

The acquisition scripts verify the source and reconstructed arrays. They save
public observations and declared forecast conditions, not hidden future fields.
Source provenance and terms are in [DATA_SOURCES.md](docs/DATA_SOURCES.md).

## Modeling tasks

| Level | Modeling setting | Main tasks |
|:---:|---|---:|
| E | Basic dynamics with simple known geometry and boundary conditions | 9 |
| M | Constitutive responses, spatial structure, or geometric effects | 11 |
| H | Coupled or constrained dynamics, and effective modeling from measurements | 13 |

Applications include heat and mass transport, reactions, waves, viscoelasticity,
electromagnetism, phase separation, and fluid dynamics. The five measured tasks
cover cell migration, three Reynolds-number settings from one PIV source, and
surface waves. They represent three application sources.

See the [full task catalog](docs/TASKS.md), [data format](docs/DATA_FORMAT.md), and
[discovery and prediction protocol](docs/PROTOCOL.md).

## Read or export one task

```python
from field2law import load_task

task, observations = load_task("physical_001")
print(task["context"])
print(observations["u"].shape)
```

```bash
python -m field2law export physical_001 workspaces/discovery
# After fixing the equation and its fitted parameters:
python -m field2law export physical_001 workspaces/conditions --conditions
```

Exported discovery directories contain the actual scientific task description
and observations, without catalog labels or evaluation inputs. Methods may use
all public observations and their own internal validation. Keep conditions,
other tasks, author-source files, and evaluation assets outside the discovery
workspace. Adapt observations to each method's native interface and document
the supplied priors and numerical processing.

## Repository layout

```text
catalog.json                     Task IDs, applications and E/M/H index
data_manifest.json               File and array checksums
data/main/<task>/discovery/       Context, fields and public observations
data/main/<task>/conditions/      Known initial and boundary conditions
data/noise/<task>/                Five paired noisy observation settings
field2law/                       Portable loading, acquisition and export tools
docs/                            Task catalog, protocol and provenance
LICENSES/                        Code, generated-data and source terms
```

Known conditions are separate from discovery observations. Reference laws,
unknown true coefficients and future interior targets are not included in this
preview. It does not yet provide a public scoring service or a portable full
benchmark evaluator. The registered experiments evaluate fixed submissions on
held-out conditions; the public evaluation release will document that interface
separately.

## Method autonomy and evidence

Field2Law uses an organizing framework from predefined libraries (L1), through
operator/grammar search (L2) and LLM-assisted workflows (L3), to agent-organized
modeling (L4). L5 describes future interactive experimentation. These levels
describe who makes the scientific decisions; E/M/H describes the task.

Prediction under new conditions measures modeling utility. For synthetic tasks,
law structure, coefficients or constitutive functions, and local dynamics provide
complementary evidence. Measured tasks have no prescribed exact PDE truth.

## Licenses and attribution

Original loader code is MIT licensed. Original synthetic fields and task
annotations are CC BY 4.0. Third-party measurements retain their own terms;
see [LICENSES](LICENSES/README.md) and [data sources](docs/DATA_SOURCES.md).
Please cite the original experimental sources when using those tasks. A paper
citation will be added when the preprint is available.
