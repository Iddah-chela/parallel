import time
from serial_word_count import serial_word_count
from parallel_word_count import parallel_word_count
from distributed_word_count import distributed_word_count
from multiprocessing import cpu_count

FILE = "../data/large.json"

def measure(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return end - start, sum(result.values())

if __name__ == "__main__":
    results = []

    # Serial
    t_serial, words_serial = measure(serial_word_count, FILE)
    results.append(("Serial", 1, t_serial))

    # Parallel (threads)
    threads = 4
    t_parallel, words_parallel = measure(parallel_word_count, FILE, threads)
    results.append(("Parallel (Threads)", threads, t_parallel))

    # Distributed (processes)
    workers = cpu_count()
    t_distributed, words_distributed = measure(distributed_word_count, FILE, workers)
    results.append(("Distributed (Processes)", workers, t_distributed))

    print("\n=== PERFORMANCE COMPARISON ===")
    print(f"{'Model':<25}{'Workers':<10}{'Time (s)':<10}")
    for r in results:
        print(f"{r[0]:<25}{r[1]:<10}{r[2]:<10.3f}")

    print("\nWord counts match:",
          words_serial == words_parallel == words_distributed)
