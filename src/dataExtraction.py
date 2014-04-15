import urllib
import csv
import pickle
import os

base_url = "http://football-data.co.uk/mmz4281/1314/"

def make_url(ticker_symbol):
    return base_url + ticker_symbol

output_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
def make_filename(ticker_symbol, directory="historicalData"):
    return output_path + "/" + directory + "/" + ticker_symbol #+ ".csv"

def pull_historical_data(ticker_symbol, directory="historicalData"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()
        
def readDataFromExcel(ticker_symbol):
    try:
        with open(output_path+"/historicalData/"+ticker_symbol+'.csv', 'rb') as csvfile:
            excelReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        
            list = []
            for row in excelReader:
                tmpList = []
                tmpList = ','.join(row)
                tmpList = tmpList.split(",")
                list.append(tmpList)
            
            print list.pop(0)
            saveStockDataToFile(ticker_symbol, list)
            
    except:
        print "error when reading/manipulating excel data"
        
def saveStockDataToFile(ticker_symbol, list):
    pickle.dump(list, open(output_path+"/objects/"+ticker_symbol, "wb"))

def readStockDataFromFile(ticker_symbol):
    list = pickle.load(open(output_path+"/objects/"+ticker_symbol, "rb"))
    
    return list

#pull_historical_data("E0.csv")
#readDataFromExcel("E0")
#list = readStockDataFromFile("E0")
#print list[1]
