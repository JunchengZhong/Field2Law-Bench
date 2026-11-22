# Discovery and independent prediction

1. Give a method the selected task's public observations and physical description.
   Methods may use all observed records and choose internal validation according
   to their native workflow.
2. Produce an explicit evolution law (or the declared constitutive flux) with
   fixed numerical parameters. Retain the method's own optimizer, search space,
   reward, candidate selection and stopping behavior.
3. Supply the known new initial/boundary conditions to the fixed model and execute
   it without refitting. Compare predicted future interiors with held-out targets.

New conditions change preparations, loading, or boundary programs within the
declared physical setting. They do not silently introduce new unknown material
parameters. PIV settings are modeled separately, with another window at the
same Reynolds number used for prediction. Cell tasks use other seeding amounts;
the wave task uses a later state of the same experiment.

Measured edge histories are supplied conditions. Their values are excluded from
the scored interior. Thus measured tasks evaluate conditional interior prediction,
not autonomous forecasting of those boundary measurements.

## Native method inputs

Different workflows need different inputs: a fixed candidate library, a numerical
feature/target table, raw fields, or tools and context. Use ordinary native
interfaces and document any derivative estimator, library or operator grammar.
The data loader adds none of these method-specific choices. Autonomy levels do
not require giving a method fewer scientific facts than its interface needs.

The principal experiment uses a maximum of 48 model generations per evolved
output, native early stopping and declared runtime limits. A separate diagnostic
uses 96; it does not replace the 48-generation results. Non-LLM methods retain
their registered native computational configurations.

## Evaluation evidence

- **Prediction:** error on new-condition future fields, normalized by registered
  public-observation scales, with each required condition accounted for.
- **Equation:** synthetic-law structure plus coefficients or constitutive functions.
- **Local dynamics:** candidate and reference responses on a common set of states.
- **Coverage and execution:** no submission, unsupported native scope, numerical
  failure, numerical sensitivity and confirmed prediction remain distinct.

These dimensions are complementary. Measured tasks have no exact-law score.
Simple prediction references, time curves and spatial profiles help interpret
real-data utility. Physics diagnostics may support individual cases; there is
no universal PDE-specific physical score imposed on every task.

## Preview scope

This release supplies discovery data, task descriptions, known prediction inputs,
and portable loaders. Hidden future targets, reference laws, full method runners
and the complete independent evaluator are outside this data/task preview.
Publishing the known-input files does not make them discovery-stage inputs.
For method runs, export the selected packet into an isolated workspace.

Expert review and paper preparation are ongoing. Corrections will receive a
documented release revision; completed experiments keep their input checksums.
