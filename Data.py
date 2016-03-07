import pickle

class Data:

    # The current table of data.
    dataSetName = ""
    data = {}

    def __init__(self):
        pass

    def importData(self):
        pass

    def loadData(self, loadString):
        try:
            inputFile = open(loadString, 'rb')
            self.data = pickle.load(inputFile)
            print('Loaded data from ' + loadString)
        except Exception as err:
            # TODO continue here
            pass

    def saveData(self, saveString):
        try:
            if (saveString == ''):
                saveString = 'mydata'
            outputFile = open(saveString, 'wb')
            pickle.dump(self.data, outputFile)
            print('Data set s% saved to %s' % (self.dataSetName, saveString))
            outputFile.close()
        except Exception as err:
            print(err)
            print('You give a valid file name and path to' +
                  ' save too relative to the current directory.')
            print('Eg. ./save/myData.dat')

    def verifyLineData(self):
        pass

    def editLineData(self):
        pass




