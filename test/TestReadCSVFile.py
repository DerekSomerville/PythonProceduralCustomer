from src.ReadCSVFile import ReadCSVFile


def test_getFileData():
    if "emailAddress" == ReadCSVFile.getFileData("customer.csv")[0][0]:
        print("Pass","test_getFileData")
    else:
        print("fail", "test_getFileData")

def main():
    test_getFileData()

if __name__ == '__main__':
    main()
