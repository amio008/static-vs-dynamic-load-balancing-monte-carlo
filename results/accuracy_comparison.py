# accuracy_comparison.py
# This script calculates and visualizes the accuracy (absolute error from actual Pi) of the three estimates.
# To run in Google Colab, simply execute the cells.

import math
import matplotlib.pyplot as plt

# Hardcoded estimates from the screenshot
estimates = {
    'Parallel Dynamic': 3.1415704,
    'Sequential': 3.1410224,
    'Parallel Static': 3.14600632
}

# Actual value of Pi
real_pi = math.pi

# Calculate absolute differences
diffs = {k: abs(v - real_pi) for k, v in estimates.items()}

# Prepare data for plotting
labels = list(diffs.keys())
values = list(diffs.values())

# Create bar plot
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'green', 'red'])
plt.ylabel('Absolute Error')
plt.title('Absolute error comparison: Closeness to Pi (Lower is better)')
plt.xticks(rotation=15)
plt.show()

# Print the differences for reference
for label, diff in diffs.items():
    print(f"{label}: Absolute Error = {diff:.8f}")