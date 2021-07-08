import csv, os

class ReadCSVFile:

    def fixWorkingDirectory():
        currentWorkingDirectory = os.getcwd()
        while "test" in currentWorkingDirectory or "src" in currentWorkingDirectory:
            os.chdir("../")
            currentWorkingDirectory = os.getcwd()

    def getFileData(fileName):
        ReadCSVFile.fixWorkingDirectory()
        fileData = []
        with open("resource/" + fileName, 'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines( self, fileName, numerOfLines):
        return self.getFileData(fileName)[-1 * numerOfLines]