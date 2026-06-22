import random
import time
import argparse
import math
from multiprocessing import Pool

def worker(n):
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
    return inside

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=5_000_000)
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()

    samples_per_worker = args.samples // args.workers

    start = time.time()
    with Pool(args.workers) as p:
        results = p.map(worker, [samples_per_worker] * args.workers)
    pi = 4 * sum(results) / args.samples
    end = time.time()

    print(f"method=static,samples={args.samples},workers={args.workers},"
          f"time={end-start:.6f},pi={pi:.8f},error={abs(pi-math.pi):.8f}")
