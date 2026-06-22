import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")
df = df[df.workers == 6]
df = df.groupby("method")["error"].median()

df.plot(kind="bar")
plt.ylabel("Absolute Error")
plt.title("Accuracy Comparison (6 cores)")
plt.grid()
plt.show()
