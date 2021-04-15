from src.ReadCSVFile import ReadCSVFile

readCSVFile = ReadCSVFile()

def loadCustomers():
    customerData = readCSVFile.getFileData("customer.csv")
    return customerData

def formatCustomers():
    display = ""
    customerData = loadCustomers()
    for counter in range(1,len(customerData)):
        display += customerData[counter][0] + "\n"
    return display