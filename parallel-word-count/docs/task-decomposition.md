## Task Decomposition

The word count problem is decomposed into the following tasks:

1. File Reading
   - Read input text file from disk

2. Data Partitioning
   - Split text into chunks for parallel processing

3. Word Counting
   - Count word frequencies independently in each chunk

4. Result Aggregation
   - Merge partial word counts into a final result

5. Output Generation
   - Display or save final word frequency results

These tasks exhibit data parallelism since each chunk can be processed independently.
