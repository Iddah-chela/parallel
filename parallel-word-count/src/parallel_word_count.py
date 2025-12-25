import time
from collections import Counter
from threading import Thread
import math

def chunkify(text, n):
    chunk_size = math.ceil(len(text) / n)
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def count_words(chunk, result, index):
    result[index] = Counter(chunk)

def parallel_word_count(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().lower().split()

    chunks = chunkify(words, num_threads)
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        t = Thread(target=count_words, args=(chunks[i], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    final_count = Counter()
    for r in results:
        final_count.update(r)

    return final_count

if __name__ == "__main__":
    start = time.time()
    counts = parallel_word_count("../data/large.json", num_threads=4)
    end = time.time()

    print("Parallel Execution Time:", end - start)
    print("Total Words:", sum(counts.values()))
