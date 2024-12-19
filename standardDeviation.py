import numpy as np
import matplotlib.pyplot as plt

# Example data
example_data = [10, 12, 23, 23, 16, 23, 21, 16, 18, 20, 12, 23, 67, 54, 98, 23, 12, 45, 67, 71, 59]

# Calculate Population Standard Deviation
population_std_dev = np.std(example_data, ddof=0)

# Calculate Sample Standard Deviation
sample_std_dev = np.std(example_data, ddof=1)

# Print results
print(f"Population Standard Deviation: {population_std_dev:.2f}")
print(f"Sample Standard Deviation: {sample_std_dev:.2f}")

# Plotting
labels = ["Population Std Dev", "Sample Std Dev"]
values = [population_std_dev, sample_std_dev]

plt.bar(labels, values, color=['blue', 'green'])
plt.title("Comparison of Standard Deviations")
plt.ylabel("Standard Deviation")
plt.show()
