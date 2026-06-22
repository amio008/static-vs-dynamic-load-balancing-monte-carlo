# src/parallel_static_pi.py
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
    workers = cpu_count()
    samples_per_worker = total_samples // workers

    start = time.time()
    with Pool(workers) as p:
        results = p.map(worker, [samples_per_worker]*workers)
    inside_total = sum(results)
    pi = 4 * inside_total / total_samples
    end = time.time()

    print(f"Estimated Pi (Static): {pi}")
    print(f"Time Taken: {end - start:.3f} seconds")
