import matplotlib.pyplot as plt

# Example data based on the description and chart
years = [2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
asia = [4.5, 4.8, 5.0, 5.1, 5.2, 5.2, 5.1, 5.0, 4.9]  # Projected population in billions
africa = [1.3, 1.7, 2.2, 2.7, 3.3, 3.9, 4.5, 5.0, 5.5]
latin_america = [0.7, 0.8, 0.9, 1.0, 1.1, 1.1, 1.2, 1.2, 1.1]
europe = [0.8, 0.8, 0.7, 0.7, 0.7, 0.6, 0.6, 0.6, 0.5]
north_america = [0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
oceania = [0.04, 0.05, 0.05, 0.06, 0.06, 0.07, 0.07, 0.07, 0.07]

# Create a figure and axis
plt.figure(figsize=(12, 6))

# Plot each region's data
plt.plot(years, asia, label='Asia', color='green')
plt.plot(years, africa, label='Africa', color='red')
plt.plot(years, latin_america, label='Latin America and the Caribbean', color='purple')
plt.plot(years, europe, label='Europe', color='gold')
plt.plot(years, north_america, label='Northern America', color='blue')
plt.plot(years, oceania, label='Oceania', color='cyan')

# Add title and labels
plt.title('UN Regional Population Projections (Billions, 2015 - 2100)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (Billions)', fontsize=12)

# Add a legend
plt.legend(loc='center right')

# Customize ticks and grid
plt.xticks(years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
