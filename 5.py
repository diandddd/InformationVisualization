import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
years = [2000, 2050, 2100]
africa = [0.814, 2.2, 4.4]  # Population in billions
asia = [3.71, 5.3, 4.9]
europe = [0.726, 0.653, 0.517]
latin_america = [0.527, 0.705, 0.687]
north_america = [0.314, 0.433, 0.478]
oceania = [0.0311, 0.048, 0.062]

# Stacking the data
bar_width = 0.5
ind = np.arange(len(years))  # The x locations for the groups

# Plot each stack
plt.bar(ind, africa, bar_width, label="Africa", color='red')
plt.bar(ind, asia, bar_width, bottom=africa, label="Asia", color='green')
plt.bar(ind, europe, bar_width, bottom=np.array(africa)+np.array(asia), label="Europe", color='blue')
plt.bar(ind, latin_america, bar_width, bottom=np.array(africa)+np.array(asia)+np.array(europe), label="Latin America and the Caribbean", color='deepskyblue')
plt.bar(ind, north_america, bar_width, bottom=np.array(africa)+np.array(asia)+np.array(europe)+np.array(latin_america), label="Northern America", color='gold')
plt.bar(ind, oceania, bar_width, bottom=np.array(africa)+np.array(asia)+np.array(europe)+np.array(latin_america)+np.array(north_america), label="Oceania", color='cyan')

# Title and labels
plt.title('UN Regional Population Projections (Billions, 2000 - 2100)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (Billions)', fontsize=12)

# X-axis ticks
plt.xticks(ind, years)

# Legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
