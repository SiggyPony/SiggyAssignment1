import cmd

from Data import Data
from Charts.PieChart import PieChart

class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program - SDPP \n'
        self.prompt = '>'
        self.data = Data()

    def do_load_data(self, line):
        'Load data from the specified file and location: load_data ./data/data4.csv'
        print('load_data')
        tableName = input("Input table name>")
        self.data.importData(line, tableName)

    def do_save_project(self, line):
        'Save project to the specified file and location: save_project ./data/myproject.dat'
        print('save_project')
        self.data.saveData(line)

    def do_load_project(self, line):
        'Load project from the specified file and location: load_project ./data/myproject.dat'
        print('load_project')
        self.data.loadData(line)

    def do_show(self, line):
        """
        Show the current loaded data tables: show
        Add a name to only show a specific table: show mydata
        """
        print('show')
        self.data.printData()

    def do_make_piechart(self):
        pass

    def do_exit(self, line):
        'Exit the program'
        return True


def main():

    print('Starting')
    controllerTemp = Controller()
    controllerTemp.cmdloop()

    #dataTemp = Data()
    #dataTemp.importData()
    #dataTemp.verifyLineData()
if __name__ == '__main__':
    main()