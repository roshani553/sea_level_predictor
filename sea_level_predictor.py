import pandas as pd
df = pd.read_csv("epa-sea-level.csv")
print(df.head())
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
 
# Perform linear regression on the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create a range of years from 1880 to 2050
years_extended = np.arange(1880, 2051)

# Calculate predicted sea levels for those years
sea_level_pred = intercept + slope * years_extended

# Plot scatter and line of best fit
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(years_extended, sea_level_pred, color='red', label='Best Fit Line (1880–2050)')

# Labels & title
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.legend()
plt.show()
# Perform linear regression on data from year 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Predict sea level from 2000 to 2050
years_recent = np.arange(2000, 2051)
sea_level_recent = intercept_recent + slope_recent * years_recent

# Plot the recent best fit line
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(years_recent, sea_level_recent, color='green', label='Best Fit Line (2000–2050)')
plt.plot(years_extended, sea_level_pred, color='red', label='Best Fit Line (1880–2050)')

plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.legend()
plt.show()
