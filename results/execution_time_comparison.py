# execution_time_comparison.py
# This script visualizes the execution times of the three Pi estimation scripts.
# Hardcoded values from your latest screenshot.
# Run this in Google Colab.

import matplotlib.pyplot as plt

# Data from the latest screenshot
methods = ['Parallel Static', 'Parallel Dynamic', 'Sequential']

times = {
    'Parallel Static': 1.032,
    'Parallel Dynamic': 0.995,
    'Sequential': 1.781
}

# Print the times
print("Execution Times:")
for method in methods:
    print(f"{method}: {times[method]:.3f} seconds")

# Bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(methods, [times[m] for m in methods], 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1'])

plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison\n(Lower is better)')
plt.ylim(0, max(times.values()) * 1.1)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
             f'{height:.3f}s',
             ha='center', va='bottom', fontweight='bold')

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Optional: Horizontal bar chart for clearer comparison
plt.figure(figsize=(8, 4))
bars_h = plt.barh(methods[::-1], [times[m] for m in methods[::-1]], 
                  color=['#45B7D1', '#4ECDC4', '#FF6B6B'])

plt.xlabel('Execution Time (seconds)')
plt.title('Execution Time Comparison\n(Lower is better)')

# Add value labels
for bar in bars_h:
    width = bar.get_width()
    plt.text(width + 0.01, bar.get_y() + bar.get_height()/2.,
             f'{width:.3f}s',
             ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.show()