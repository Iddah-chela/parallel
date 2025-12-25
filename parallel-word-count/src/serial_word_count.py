import time
from collections import Counter

def serial_word_count(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower().split()
    return Counter(text)

if __name__ == "__main__":
    start = time.time()
    counts = serial_word_count("../data/large.json")
    end = time.time()

    print("Serial Execution Time:", end - start)
    print("Total Words:", sum(counts.values()))
