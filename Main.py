import cmd, re

from Data import Data
from Charts.PieChart import PieChart


class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program - SDPP \n'
        self.prompt = '>'
        self.data = Data()

    def do_load_data(self, line):
        'Load data from the specified file and location: \
load_data ./data/data4.csv'
        print('load_data')
        tableName = input("Input table name>")
        self.data.importData(line, tableName)

    def do_save_project(self, line):
        'Save project to the specified file and location: \
save_project ./data/myproject.dat'
        print('save_project')
        self.data.saveData(line)

    def do_load_project(self, line):
        'Load project from the specified file and location: \
load_project ./data/myproject.dat'
        print('load_project')
        self.data.loadData(line)

    def do_show(self, line):
        """
        Show the current loaded data tables: show
        Add a name to only show a specific table: show mydata
        """
        print('show')
        self.data.printData()

    def do_make_piechart(self, line):
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
            listOfColumns = listOfColumns + (self.data.data[tableName][col][0]) + " "
        print(listOfColumns)
        chartLabels = input("Input column for labels>")
        for col in range(0, len(self.data.data[tableName][0])):
            if self.data.data[tableName][col][0] == chartLabels:
                chartLabelsData = self.data.data[tableName][col][:]
        if (chartLabelsData == None):
            print("Must give a valid column name.")
            return;
        del chartLabelsData[0]
        print(chartLabelsData)
        # Get and verify table data information
        chartSizes = input("Input column for values>")
        for col in range(0, len(self.data.data[tableName][0])):
            if self.data.data[tableName][col][0] == chartSizes:
                for item in range(1, len(self.data.data[tableName][col])):
                    print('checking value %s from column meets re ^[0-9]*$' % (self.data.data[tableName][col][item]))
                    if not(re.match('^[0-9]*$', self.data.data[tableName][col][item])):
                        print("False")
                        print("Column must only contain numbers")
                        return
                chartSizesData = self.data.data[tableName][col][:]
            else:
                print("Must give a valid column name.")

        del chartSizesData[0]
        print(chartSizesData)

        pieChart = PieChart([tableTitle, chartLabelsData, chartSizesData])
        pieChart.drawChart()

    def do_exit(self, line):
        'Exit the program'
        return True


def main():
    #if re.match('^[A-Z][0-9]{3}$','A344'):
    #    print("True")
    #else:
    #    print("False")

    print('Starting')
    controllerTemp = Controller()
    controllerTemp.cmdloop()

    #dataTemp = Data()
    #dataTemp.importData()
    #dataTemp.verifyLineData()

if __name__ == '__main__':
    main()
