import cmd
import pickle
import csv
import re
import matplotlib.pyplot as plt


class Data:

    data = {}
    #    data2 = {'table1': [
    #        ['col1', 11, 12, 13, 14, 15 ],
    #        ['col2', 21, 22, 23, 24, 25 ],
    #        ['col3', 31, 32, 33, 34, 35 ]
    #        ],
    #        'table2': [
    #        ['col1', 51, 12, 13, 14, 15 ],
    #        ['col2', 51, 22, 23, 24, 25 ],
    #        ['col3', 51, 32, 33, 34, 35 ]
    #    ]}
    #        'table2': {
    #        'col1': [ 51, 12, 13, 14, 15 ],
    #        'col2': [ 51, 22, 23, 24, 25 ],
    #        'col3': [ 51, 32, 33, 34, 35 ]

    dataGREP = ['^[A-Z][0-9]{3}$',
                '^(M|F)$',
                '^[0-9]{2}$',
                '^[0-9]{3}$',
                '^(Normal|Overweight|Obesity|Underweight)$',
                '^[0-9]{2,3}$']

    def __init__(self):
        pass

    def importData(self, importString, tableName):
        try:
            with open(importString) as csvfile:
                datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
                columns = []
                loopCounter = 0
                for row in datareader:
                    for (i, v) in enumerate(row):
                        if loopCounter == 0:
                            column = [v]
                            columns.append(column)
                            # print(column)
                        else:
                            columns[i].append(v)
                    loopCounter += 1
                # print(columns)
            self.data[tableName] = columns
            # print(self.data)
            self.printData()
            print('Data loaded')
            return self.verifyLineData(tableName)
        except Exception as err:
            print(err)
            print('You must give a valid csv file name and path .')
            print('Eg. ./data3.csv')

    def printData(self):
        # TODO find largest value and space each row appropriately
        print('Printing loaded tables data')
        line = ''
        for tableName, table in self.data.items():
            print(tableName)
            for i in range(0, len(table[0])):
                for x in range(0, len(table)):
                    line = line + '   ' + (str(table[x][i]))
                print(line)
                line = ''

    def loadProject(self, loadString):
        try:
            inputFile = open(loadString, 'rb')
            self.data = pickle.load(inputFile)
            print('Loaded data from ' + loadString)
        except Exception as err:
            print(err)
            print('You need to give the address and \
             name of a valid file to load.')
            pass

    def saveProject(self, saveString):
        try:
            if (saveString == ''):
                saveString = 'mydata'
            outputFile = open(saveString, 'wb')
            pickle.dump(self.data, outputFile)
            print('Current project has been saved to %s' % (saveString))
            outputFile.close()
        except Exception as err:
            print(err)
            print('You give a valid file name and path to' +
                  ' save too relative to the current directory.')
            print('Eg. ./save/myData.dat')

    def verifyLineData(self, tableName):
        tableError = []
        errorCount = 0
        print("Verifying table %s" % tableName)
        # i = row num
        for row in range(1, len(self.data[tableName][0])):
            # x = column num.
            for col in range(0, len(self.data[tableName])):
                # print('checking value %s from column %s meets re %s' %
                # (x, str(self.data[tableName][x][i]), self.dataGREP[x]))
                if re.match(self.dataGREP[col],
                            str(self.data[tableName][col][row])):
                    pass
                    # print("True")
                else:
                    # print("False")
                    tableError.append([col, row])
                    errorCount += 1
        if errorCount > 0:
            print("Data error detected in new table")
            for errorDetails in tableError:
                print("Error in coloumn %s, row %s where value "
                      "'%s' does not match expression '%s'" %
                      (errorDetails[0], errorDetails[1],
                       str(self.data[tableName]
                           [errorDetails[0]][errorDetails[1]]),
                       self.dataGREP[errorDetails[0]]))
            print("Dropping table. Please fix errors and reload data.")
            del self.data[tableName]
            return False
        else:
            print("Data verified")
            return True


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
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.figtext(0.5, 0.965, self.chartTitle, ha='center',
                    color='black', weight='bold', size='large')
        plt.axis('equal')
        plt.show()


class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program - SDPP \n'
        self.prompt = '>'
        self.data = Data()

    def do_load_data(self, importString):
        """
Load data from the specified file and location: load_data ./data/data4.csv
Will ask for name of new table.
        """
        l = importString.split()
        if len(l) != 1:
            print("Invalid number of arguments")
            return
        print('load_data')
        tableName = input("Input table name>")
        l = tableName.split()
        if len(l) != 1:
            print("Table name can't be blank and must not contain spaces.")
            return
        self.data.importData(importString, tableName)

    def do_save_project(self, saveString):
        """
Save project to the specified file and location: save_project myproject.dat
        """
        l = saveString.split()
        if len(l) != 1:
            print("Invalid number of arguments")
            return
        print('save_project')
        self.data.saveProject(saveString)

    def do_load_project(self, loadString):
        """
Load project from the specified file and location: load_project myproject.dat
        """
        l = loadString.split()
        if len(l) != 1:
            print("Invalid number of arguments")
            return
        print('load_project')
        self.data.loadProject(loadString)

    def do_show(self, line):
        """
Show the current loaded data tables: show
        """
        print('show')
        self.data.printData()

    def do_make_piechart(self, line):
        """
Will create Pie Chart.
Will ask for,
    Table title (for chart output)
    Source table (to take data from)
    Labels column (column in table to use as labels in Pie Chart)
    Data column (column in table to use as data for Pie Chart)
        must be numeric
        """
        tableTitle = input("Input title for new table>")
        tableName = input("Input source table name>")
        if not(tableName in self.data.data.keys()):
            print("Table not found.")
            return

        # Show columns
        chartLabelsData = None
        chartSizesData = None
        listOfColumns = "Coloumns in " + tableName + ": "
        for col in range(0, len(self.data.data[tableName][0])):
            listOfColumns = listOfColumns + \
                            (self.data.data[tableName][col][0]) + " "
        print(listOfColumns)
        chartLabels = input("Input column for labels>")
        for col in range(0, len(self.data.data[tableName][0])):
            if self.data.data[tableName][col][0] == chartLabels:
                chartLabelsData = self.data.data[tableName][col][:]
        if (chartLabelsData is None):
            print("Must give a valid column name.")
            return
        del chartLabelsData[0]
        print(chartLabelsData)
        # Get and verify table data information
        chartSizes = input("Input column for values>")
        for col in range(0, len(self.data.data[tableName][0])):
            if self.data.data[tableName][col][0] == chartSizes:
                for item in range(1, len(self.data.data[tableName][col])):
                    if not(re.match('^[0-9]*$',
                                    self.data.data[tableName][col][item])):
                        print("False")
                        print("Column must only contain numbers")
                        return
                chartSizesData = self.data.data[tableName][col][:]
                del chartSizesData[0]
                print(chartSizesData)

                pieChart = PieChart([tableTitle, chartLabelsData,
                                     chartSizesData])
                pieChart.drawChart()
                return
        print("Must give a valid column name.")
        return

    def do_exit(self, line):
        'Exit the program'
        return True


def main():
    print('Starting')
    controllerTemp = Controller()
    controllerTemp.cmdloop()


if __name__ == '__main__':
    main()
