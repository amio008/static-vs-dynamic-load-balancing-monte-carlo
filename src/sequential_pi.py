# src/sequential_pi.py
import random
import time

def estimate_pi(n_samples):
    inside = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n_samples

if __name__ == "__main__":
    samples = 5_000_000
    start = time.time()
    pi = estimate_pi(samples)
    end = time.time()

    print(f"Estimated Pi: {pi}")
    print(f"Time Taken: {end - start:.3f} seconds")
