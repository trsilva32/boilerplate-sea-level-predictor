import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,10))
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    # Get Values of LinearReg
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x1 = list(range(1880,2050))
    y1 = []
    for i in x1:
      y1.append(intercept + slope * i)
    plt.plot(x1,y1, 'r' , label = 'Best Fit line 1')

    # Create second line of best fit
    x2 = df.Year[df['Year']>=2000]
    y2 = df[df['Year']>=2000]['CSIRO Adjusted Sea Level']

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)

    x2 = list(range(2000,2050))
    y2 = [] 
    
    for i in x2:
      y2.append(intercept2 + slope2 * i)

    plt.plot(x2,y2, 'b', label = 'Best Fit Line 2')
    plt.legend()


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
