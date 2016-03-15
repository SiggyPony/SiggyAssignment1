import matplotlib.pyplot as plt


class PieChart:
    chartTitle = None
    chartLabels = None
    chartSizes = None

    def __init__(self, data):
        self.chartTitle = data[0]
        self.chartLabels = data[1]
        self.chartSizes = data[2]

    def drawChart(self):
        plt.pie(self.chartSizes, None, self.chartLabels, None,
                autopct='%1.1f%%', pctdistance=0.90,
                shadow=True, startangle=90)
        plt.figtext(0.5, 0.965, self.chartTitle, ha='center',
                    color='black', weight='bold', size='large')
        plt.axis('equal')
        plt.show()
