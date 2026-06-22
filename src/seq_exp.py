import random
import time
import argparse
import math

def estimate_pi(n):
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=5_000_000)
    args = parser.parse_args()

    start = time.time()
    pi = estimate_pi(args.samples)
    end = time.time()

    print(f"method=sequential,samples={args.samples},workers=1,"
          f"time={end-start:.6f},pi={pi:.8f},error={abs(pi-math.pi):.8f}")
