# Air Quality Data Analysis Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("air_quality.csv")

# Explore dataset
print(data.head())
print(data.info())

# Check missing values
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

print(data.describe())

# Group pollution by city
city_pm = data.groupby("city")["pm2_5"].mean()

# Sort cities by pollution
print("Pollution order:")
print(city_pm.sort_values(ascending=False))

# Bar graph
city_pm.plot(kind="bar")
plt.title("Average PM2.5 Pollution by City")
plt.xlabel("City")
plt.ylabel("PM2.5 Level")
plt.savefig("pollution_by_city.png")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(data["temperature"], data["pm2_5"])
plt.xlabel("Temperature")
plt.ylabel("PM2.5")
plt.title("Temperature vs Pollution")
plt.show()

# Histogram
plt.figure()
plt.hist(data["pm2_5"], bins=20)
plt.title("Distribution of PM2.5 Pollution")
plt.xlabel("PM2.5")
plt.ylabel("Frequency")
plt.show()

# Correlation
correlation = data.corr(numeric_only=True)
print(correlation)