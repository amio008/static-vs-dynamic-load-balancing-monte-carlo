import subprocess
import csv

workers = [1, 2, 3, 4, 5, 6]
samples = 5_000_000
runs = 3

with open("results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["method","samples","workers","time","pi","error"])

    for w in workers:
        for _ in range(runs):
            for cmd in [
                ["python", "src/seq_exp.py", "--samples", str(samples)],
                ["python", "src/static_exp.py", "--samples", str(samples), "--workers", str(w)],
                ["python", "src/dynamic_exp.py", "--samples", str(samples), "--workers", str(w)]
            ]:
                out = subprocess.check_output(cmd).decode().strip()
                fields = dict(x.split("=") for x in out.split(","))
                writer.writerow([
                    fields["method"],
                    fields["samples"],
                    fields["workers"],
                    fields["time"],
                    fields["pi"],
                    fields["error"]
                ])
