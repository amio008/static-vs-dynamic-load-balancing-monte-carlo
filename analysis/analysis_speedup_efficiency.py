import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")
base = df[(df.method=="sequential") & (df.workers==1)].time.median()

for m in ["static","dynamic"]:
    sub = df[df.method==m].groupby("workers")["time"].median()
    speedup = base / sub
    efficiency = speedup / sub.index

    plt.plot(sub.index, speedup, marker="o", label=f"{m}-speedup")

plt.xlabel("Workers")
plt.ylabel("Speedup")
plt.title("Speedup vs Workers")
plt.legend()
plt.grid()
plt.show()
