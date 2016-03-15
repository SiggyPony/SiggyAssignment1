import pickle
import csv
import re


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

    def importData(self, importString='data3.csv', tableName='data'):
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
    """
            for row in datareader:
                print(len(row))

                for x in range(0, len(row)):


                for (i,v) in enumerate(row):
                    print(str(i) + ' ' + str(v))
                    #columns[i].append(v)
    """

    def printData(self):
        # TODO find largest value and space each row appropriately
        print('Printing loaded tables data')
        line = ''
        for tableName, table  in self.data.items():
            print(tableName)
            for i in range(0, len(table[0])):
                for x in range(0, len(table)):
                    line = line + '   ' + (str(table[x][i]))
                print(line)
                line = ''
 #       print(tableName)
 #       for i in range(0, len(self.data[tableName][0])):
 #           for x in range(0, len(self.data[tableName])):
 #               line = line + '   ' + (str(self.data[tableName][x][i]))
 #           print(line)
 #           line = ''

    def loadProject(self, loadString):
        try:
            inputFile = open(loadString, 'rb')
            self.data = pickle.load(inputFile)
            print('Loaded data from ' + loadString)
        except Exception as err:
            print(err)
            print('You need to give the address and name of a valid file to load.')
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




    def verifyLineData(self, tableName='data'):
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
                       str(self.data[tableName][errorDetails[0]][errorDetails[1]]),
                       self.dataGREP[errorDetails[0]]))
            print("Dropping table. Please fix errors and reload data.")
            del self.data[tableName]
            return False
        else:
            print("Data verified")
            return True

