# Week 2 Performance Analysis

## Test Environment
- Language: Python 3
- Platform: Windows
- Execution Model: Shared-memory multithreading
- Dataset: large.txt

## Execution Times

| Version   | Threads | Execution Time (seconds) |
|----------|---------|--------------------------|
| Serial   | 1       | 0.36                     |
| Parallel | 4       | 0.41                     |

## Speedup Calculation

Speedup = T_serial / T_parallel

Speedup = 0.36 / 0.41 ≈ 0.87

## Analysis
The parallel implementation using multithreading was slower than the serial
implementation. This is due to Python’s Global Interpreter Lock (GIL), which
prevents true parallel execution of CPU-bound tasks. Additionally, overhead
from thread creation and synchronization reduced performance gains.

## Conclusion
Multithreading in Python is not suitable for CPU-intensive tasks such as word
counting. This motivated the use of multiprocessing in Week 3 to achieve true
parallelism.
