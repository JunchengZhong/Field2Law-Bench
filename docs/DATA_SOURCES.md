# Experimental sources and transformations

## PC3 scratch-assay profiles

Original experiments: Jin et al., *Reproducibility of scratch assays is affected
by the initial degree of confluence: Experiments, modelling and model selection*,
Journal of Theoretical Biology 390 (2016), 136–145.
[DOI](https://doi.org/10.1016/j.jtbi.2015.10.040).

Digital source: [jlager/BINNs](https://github.com/jlager/BINNs), revision
`41d4b8f3e06597449f76750cf840d2bee7111143`, `Data/cell_density_profiles.npy`.
Associated modeling paper: Lagergren et al. (2020),
[Biologically-informed neural networks guide mechanistic modeling from sparse experimental data](https://doi.org/10.1371/journal.pcbi.1008462).

The loader drops the leftmost spatial bin as in the author's data processing,
converts coordinates to mm, time to days, and density to 1000 cells/mm². It keeps
individual replicates. Public seeding amounts are 10000, 14000, 16000 and 20000;
new conditions use 12000 and 18000, with three replicates each. Measured edge
histories condition prediction. This split and boundary-conditioned evaluation
are Field2Law adaptations, not the authors' reported evaluation.

No independent redistribution license for this measurement file was established.
The repository therefore includes task documents and a fixed-source acquisition
script rather than copies of the measured arrays. The paper's publication license
is not substituted for the repository data's terms.

## Cylinder-wake PIV

Peter Renn (data collector), Emily Palmer (data curator), Morteza Gharib
(supervisor), *Particle-image-velocimetry data of cylinder wakes*, CaltechDATA,
version 2. [Dataset DOI](https://doi.org/10.22002/g2z1f-nex65).
The dataset metadata specifies [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Field2Law extracts the first 100-frame sequence at each of Re240, Re910 and Re2520
for discovery; the next sequence defines the separate prediction conditions.
Measurements are converted to NPZ, with local array coordinates `n,s` and the
source velocity channels retained. Values are not rotated, sign-corrected,
projected to a divergence-free field or smoothed. Known future strips contain
the outer three grid cells. The scored interior excludes those strips and a
guard cell. There is no supplied pressure observation or exact two-dimensional
Navier–Stokes reference law.

These are selected excerpts and adapted modeling tasks, not redistribution of
the full source collection. Three Reynolds numbers are three settings from one
source, not three independent application sources. Source creators do not endorse
the benchmark or its derived conclusions.

## Wave-tank surface elevations

Source study: Xu et al., Nature Communications 16, 10255 (2025),
[DOI](https://doi.org/10.1038/s41467-025-65114-2).
Measurement sample provided through the
[Scientific Artificial Intelligence Lab's KD repository](https://github.com/Scientific-Artificial-Intelligence-Lab/kd),
revision `b691ec950ce235cae37a2fa669cd39f425c5f1ad`,
`src/kd/_assets/data/wave_breaking_N_G2Tp12A100_broad.npz`.
Its [NOTICE](https://github.com/Scientific-Artificial-Intelligence-Lab/kd/blob/b691ec950ce235cae37a2fa669cd39f425c5f1ad/NOTICE)
describes Imperial College London measurements redistributed with the authors'
permission. This is distinct from the package's general software license.

The acquisition script selects the central continuous camera view, determined
by coordinate order, and linearly samples each frame onto 129 spatial points
inside its measured coverage. No temporal smoothing or interpolation across
camera gaps is added. The first 39 frames are public observations. A later
initial profile and two five-node measured edge strips specify prediction.
Only observations and known conditions are saved; future interior measurements
are not written. The case is later-state prediction within the same experiment.

Measurements are obtained from the fixed author-hosted source by the user-side
script; this repository does not relicense or redistribute that source file.
Both measured acquisition scripts accept `--source-file` for an existing copy
and reject unexpected source contents.
