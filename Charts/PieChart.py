import matplotlib.pyplot as plt

"""
Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.

import matplotlib.pyplot as plt


# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()
"""

class PieChart:
    chartTitle = None
    chartLabels = None
    chartSizes = None

    def __init__(self, data):
        self.chartTitle = data[0]
        self.chartLabels = data[1]
        self.chartSizes = data[2]

    def drawChart(self):
        plt.pie(self.chartSizes, None, self.chartLabels, None, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.figtext(0.5, 0.965, self.chartTitle, ha='center', color='black', weight='bold', size='large')
        plt.axis('equal')
        plt.show()


