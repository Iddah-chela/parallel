## Design Overview

The system uses a master–worker architecture.

- The master process handles file reading, chunking, task distribution,
  and result aggregation.
- Worker threads or processes independently count words in assigned chunks.
- Load balancing is achieved by assigning chunks dynamically to workers.

## Parallelization Strategy
- Data parallelism is applied by splitting the input file into chunks.
- Shared-memory parallelism will be implemented using multithreading.
- Distributed execution will be simulated using multiprocessing.

## Performance Metrics
- Execution time
- Speedup
- Efficiency
