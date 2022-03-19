import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv(r"C:\Users\shawn\Desktop\Python Learning\epa-sea-level.csv", delimiter=",")


    # Create scatter plot
    plt.figure(figsize=(8, 8))
    df.plot(kind="scatter", x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    range1 = list(range(1880, 2051))  # range years assignment asked for
    values1 = []  # calculated y values go here
    line1 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    for year in range1:  # create list of values for line of best fit
        values1.append(line1.intercept + line1.slope*year)

    plt.plot(range1, values1)


    # Create second line of best fit
    range2 = list(range(2000, 2051))
    values2 = []
    predict2 = df.loc[df["Year"] >= 2000]
    line2 = linregress(x=predict2["Year"], y=predict2["CSIRO Adjusted Sea Level"])
    for year in range2:
        values2.append(line2.intercept + line2.slope*year)

    plt.plot(range2, values2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()