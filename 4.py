import matplotlib.pyplot as plt

# Data for the chart
regions = [
    "Africa",
    "Asia",
    "Latin America and the Caribbean",
    "Northern America",
    "Oceania",
    "Europe"
]
population_change = [1291, 874, 150, 75.3, 17.3, -31.6]  # Population change in millions
colors = ['red', 'green', 'purple', 'gold', 'cyan', 'blue']  # Custom colors for each bar

# Create the horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(regions, population_change, color=colors)

# Add data labels to the bars
for bar, value in zip(bars, population_change):
    plt.text(
        bar.get_width() + (10 if value > 0 else -50),  # Adjust position based on value sign
        bar.get_y() + bar.get_height() / 2,
        f'{value:.1f}',
        va='center',
        ha='left' if value > 0 else 'right',
        fontsize=10
    )

# Add title and labels
plt.title('Regional Population Change (2015 - 2050)', fontsize=14)
plt.xlabel('Absolute Population Change (Millions)', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
