import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(12, 6))
    axes.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    first_x = pd.Series(range(1880, 2051))
    axes.plot(first_x, first_line.intercept + first_line.slope*first_x, color='red', label='Fitted line')

    # Create second line of best fit
    second_line = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    second_x = pd.Series(range(2000, 2051))
    axes.plot(second_x, second_line.intercept + second_line.slope*second_x, color='green', label='Fitted line dcc')

    # Add labels and title
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()