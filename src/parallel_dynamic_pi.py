# src/parallel_dynamic_pi.py
import random
import time
from multiprocessing import Pool, cpu_count

def worker(n):
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
    return inside

if __name__ == "__main__":
    total_samples = 5_000_000
    chunk_size = 50_000
    tasks = total_samples // chunk_size

    start = time.time()
    with Pool(cpu_count()) as p:
        results = p.imap(worker, [chunk_size]*tasks)
        inside_total = sum(results)

    pi = 4 * inside_total / total_samples
    end = time.time()

    print(f"Estimated Pi (Dynamic): {pi}")
    print(f"Time Taken: {end - start:.3f} seconds")
