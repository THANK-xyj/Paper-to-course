# Paper Analysis

Use this before designing the course. The goal is not a generic summary; the goal is a teachable map of the paper's reasoning.

## Analysis Passes

1. **Skim for identity**
   - Title, authors, venue/date if available
   - Abstract thesis
   - Section structure
   - Figure/table inventory

2. **Trace the argument**
   - What problem is expensive, unsolved, unreliable, or misunderstood?
   - What gap does the paper claim prior work leaves?
   - What is the paper's central bet?
   - What would have to be true for the method to work?

3. **Map the method**
   - Inputs and assumptions
   - Core representation or model
   - Training/inference/control pipeline
   - Outputs and decision points
   - Where the novelty lives

4. **Audit the evidence**
   - Which experiment supports which claim?
   - Which baselines make the comparison fair or weak?
   - Which metric matters most for the paper's thesis?
   - Which ablation isolates the claimed contribution?

5. **Find boundaries**
   - Stated limitations
   - Unstated assumptions
   - Fragile dependencies: data, scale, hardware, labels, simulator fidelity, human evaluation
   - Reproduction blockers

## Course Notes Template

Use this temporary structure while analyzing:

```markdown
# Paper Map

## Thesis
[one sentence]

## Why It Matters
[practical reason]

## Claim -> Evidence Map
- Claim:
  Evidence:
  Weakness:

## Method Pipeline
1.
2.
3.

## Key Equations or Algorithms
- Name:
  Meaning:
  Variables:
  Where used:

## Figure/Table Inventory
- Figure 1:
  Teaches:
  Risk:

## Reproduction Path
- Code:
- Data:
- Parameters:
- Missing details:
```

## Red Flags

- Abstract claim is broader than experiments.
- Baselines are old, weak, or missing obvious competitors.
- Metrics do not match the real-world objective.
- Ablations remove too many things at once.
- Human evaluation lacks clear rubric or agreement.
- Simulation results are presented like real-world deployment.
- The paper reports averages but hides variance or failure cases.
