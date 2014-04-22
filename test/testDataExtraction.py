import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src')))
import dataExtraction

dataExtraction.pull_historical_data("E0.csv")
dataExtraction.readDataFromExcel("E0")
list = dataExtraction.readStockDataFromFile("E0")
print list[1]