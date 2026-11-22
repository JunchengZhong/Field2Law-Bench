# Task catalog

The 33 main modeling tasks and five paired noise controls.
E/M/H describes modeling demands; measured tasks belong to H.
Task descriptions below are a reader index; use only the exported discovery packet as method input.

| Task | Application | Level | Origin | Data |
|---|---|:---:|---|---|
| `diffusion_p1_01` | Concentration-dependent planar diffusion | M | synthetic | included |
| `pattern_stable_r01` | Decay of nonlinear spatial perturbations | M | synthetic | included |
| `pattern_unstable_r01` | Competing long-wave growth and short-wave smoothing | H | synthetic | included |
| `reaction_second_r01` | Concentration-dependent consumption | M | synthetic | included |
| `saturation_hyperbolic_r01` | Saturating consumption with a linear dilute response | M | synthetic | included |
| `saturation_sigmoidal_r01` | Saturating consumption with a suppressed dilute response | M | synthetic | included |
| `transport_affine_r01` | Density-dependent transport | M | synthetic | included |
| `wave_kdv_r01` | Weakly nonlinear dispersive waves | M | synthetic | included |
| `annular_heat_01` | Boundary heating of a plate with a hole | M | synthetic | included |
| `autocatalysis_bimolecular_r01` | Two-species autocatalytic feedback | H | synthetic | included |
| `diffusion_positive_diagonal_r01` | Planar heat transport along known material axes | E | synthetic | included |
| `gray_scott_3d_01` | Three-dimensional two-species reaction and diffusion | H | synthetic | included |
| `heat_3d_01` | Heating a three-dimensional body through its faces | M | synthetic | included |
| `kelvin_voigt_r01` | Small-amplitude waves in a viscoelastic medium | E | synthetic | included |
| `maxwell_polarization_r01` | Polarized propagation in a dielectric medium | M | synthetic | included |
| `navier_stokes_vorticity_r01` | Planar vorticity transport | H | synthetic | included |
| `physical_001` | Heat redistribution in a uniform insulated rod | E | synthetic | included |
| `physical_002` | Tracer transport in a circulating channel | E | synthetic | included |
| `physical_003` | First-order consumption in a closed medium | E | synthetic | included |
| `physical_004` | Heat transport through a graded material | M | synthetic | included |
| `physical_005` | Material interfaces and heat-exchange boundaries | H | synthetic | included |
| `measured_cells_loading` | PC3 scratch-assay density recovery | H | measured | author download |
| `measured_piv_fixed_Re240` | Measured cylinder-wake velocities at Re = 240 | H | measured | included |
| `measured_piv_fixed_Re910` | Measured cylinder-wake velocities at Re = 910 | H | measured | included |
| `measured_piv_fixed_Re2520` | Measured cylinder-wake velocities at Re = 2520 | H | measured | included |
| `acoustic_pulse_01` | Acoustic pulses in a uniform medium | E | synthetic | included |
| `linear_dispersion_01` | Linear dispersion of small-amplitude waves | E | synthetic | included |
| `planar_cooling_01` | Boundary cooling of a uniform plate | E | synthetic | included |
| `species_exchange_01` | Reversible exchange between two species | E | synthetic | included |
| `phase_separation_01` | Phase separation in a closed mixture | H | synthetic | included |
| `shallow_water_01` | Free-surface gravity waves in shallow water | H | synthetic | included |
| `excitable_recovery_01` | Activation and recovery in an excitable medium | H | synthetic | included |
| `measured_wave_window` | Measured wave-tank surface elevations | H | measured | author download |

## Paired noise controls

Five existing synthetic tasks have a separate 1% observation-noise setting. They do not increase the main-task count and have not been promoted to H.

- `diffusion_p1_01`
- `saturation_hyperbolic_r01`
- `saturation_sigmoidal_r01`
- `physical_004`
- `excitable_recovery_01`
