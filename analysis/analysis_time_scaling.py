import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")
df = df.groupby(["method","workers"])["time"].median().reset_index()

for m in df.method.unique():
    sub = df[df.method == m]
    plt.plot(sub.workers, sub.time, marker="o", label=m)

plt.xlabel("Workers")
plt.ylabel("Execution Time (s)")
plt.title("Time Scaling with CPU Cores")
plt.legend()
plt.grid()
plt.show()
