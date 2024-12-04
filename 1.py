import matplotlib.pyplot as plt

# Data for the chart
years = [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050]
nigeria_population = [182.2, 206.1, 234.2, 263.8, 295.1, 328.4, 362.4, 398.5]
us_population = [321.4, 331.9, 342.1, 353.1, 364.1, 374.8, 381.5, 386.2]

# Create the figure and axis
plt.figure(figsize=(10, 6))

# Plot data for Nigeria and the US
plt.plot(years, nigeria_population, label='Nigeria', color='green', linewidth=2)
plt.plot(years, us_population, label='United States of America', color='orange', linewidth=2)

# Add markers to the key points in 2045
plt.scatter([2045], [362.4], color='green', s=100, label=None)
plt.scatter([2045], [381.5], color='orange', s=100, label=None)

# Annotate the markers
plt.text(2045, 362.4, '362.4', color='white', fontsize=10, ha='center', va='center', bbox=dict(facecolor='green', edgecolor='none'))
plt.text(2045, 381.5, '381.5', color='white', fontsize=10, ha='center', va='center', bbox=dict(facecolor='orange', edgecolor='none'))

# Add title and labels
plt.title('Projected Population of Nigeria and the United States (Millions)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (Millions)', fontsize=12)

# Customize ticks
plt.xticks(years, fontsize=10)
plt.yticks(fontsize=10)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
