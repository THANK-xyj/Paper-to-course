# Experiment Logic

Use this for empirical, ML, systems, scientific, or benchmark papers.

## What to Extract

- Research question for each experiment
- Dataset or simulation setup
- Baselines and why they matter
- Metrics and what they measure
- Main result
- Ablation result
- Robustness or sensitivity checks
- Failure cases

## Teaching Experiments

Experiments should be taught as a courtroom evidence chain:

```text
Claim -> Test -> Comparator -> Metric -> Result -> Caveat
```

If an experiment does not support a specific claim, do not present it as proof. Say what it actually supports.

## Common Experiment Modules

- "Does it beat prior work?"
- "Which component matters?"
- "Does it scale?"
- "Does it generalize?"
- "Where does it fail?"

## Quiz Styles

- "A new baseline beats the method on the real-world metric. Which claim is weakened?"
- "The ablation removes two components at once. What can you no longer conclude?"
- "The method works in simulation. What extra evidence would you need before deployment?"
