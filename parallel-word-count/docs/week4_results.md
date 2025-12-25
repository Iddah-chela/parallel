# Week 4 – Integrated Performance Evaluation

## Performance Summary

| Model                  | Workers | Time (s) |
|-----------------------|---------|----------|
| Serial                | 1       | 0.306     |
| Parallel (Threads)    | 4       | 0.319     |
| Distributed (Process) | 8       | 0.979     |

## Observations
- Serial execution was fastest for the selected dataset.
- Multithreading did not improve performance due to Python's GIL.
- Distributed processing incurred higher overhead from process creation
  and inter-process communication.
- All implementations produced identical word counts, confirming correctness.

## Discussion
The results demonstrate that parallel and distributed systems introduce
overhead that can outweigh performance benefits for small or moderate datasets.
This highlights the importance of workload size, task granularity, and system
architecture when designing parallel applications.
