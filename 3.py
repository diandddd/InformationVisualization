import matplotlib.pyplot as plt

# Data for the chart
countries = [
    "India",
    "Nigeria",
    "Pakistan",
    "Democratic Republic of the Congo",
    "Ethiopia",
    "United States of America",
    "Indonesia",
    "Uganda"
]
population_growth = [394, 216, 121, 118, 89.1, 67.1, 64.7, 62.8]  # Absolute growth in millions

# Define custom colors for each region
colors = [
    'orange',  # India (Asia)
    'green',   # Nigeria (Africa)
    'blue',    # Pakistan (Asia)
    'red',     # Democratic Republic of the Congo (Africa)
    'purple',  # Ethiopia (Africa)
    'gold',    # United States of America (North America)
    'cyan',    # Indonesia (Asia)
    'pink'     # Uganda (Africa)
]

# Create the horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(countries, population_growth, color=colors)

# Add data labels to the bars
for bar, value in zip(bars, population_growth):
    plt.text(
        bar.get_width() + 5,  # Position text slightly to the right of the bar
        bar.get_y() + bar.get_height() / 2,
        f'{value:.1f}',  # Format the number with one decimal place
        va='center',
        fontsize=10
    )

# Add title and labels
plt.title('Population Growth between 2015 and 2050', fontsize=14)
plt.xlabel('Absolute Increase (Millions)', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
