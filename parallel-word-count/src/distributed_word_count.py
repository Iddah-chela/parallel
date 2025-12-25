import time
from collections import Counter
from multiprocessing import Pool, cpu_count
import math

def count_words(chunk):
    return Counter(chunk)

def chunkify(data, n):
    chunk_size = math.ceil(len(data) / n)
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def distributed_word_count(filename, workers):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().lower().split()

    chunks = chunkify(words, workers)

    with Pool(processes=workers) as pool:
        results = pool.map(count_words, chunks)

    final_count = Counter()
    for r in results:
        final_count.update(r)

    return final_count

if __name__ == "__main__":
    workers = cpu_count()

    start = time.time()
    counts = distributed_word_count("../data/large.json", workers)
    end = time.time()

    print("Distributed Execution Time:", end - start)
    print("Total Words:", sum(counts.values()))
