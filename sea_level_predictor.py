import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('Sea Level Predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051, 1)
    line_fit = slope * years_extended + intercept
    plt.plot(years_extended, line_fit, 'r', label='Best Fit Line (All Data)')

    # Create second line of best fit (from year 2000)
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(recent_data['Year'], 
                                                                          recent_data['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051, 1)
    line_fit_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line_fit_recent, 'g', label='Best Fit Line (From 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Set x-axis ticks
    plt.xticks(np.arange(1850, 2076, 25))

    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()