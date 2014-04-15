import os
import sys

from os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src')) import pull_historical_data

pull_historical_data("E0.csv")
readDataFromExcel("E0")
list = readStockDataFromFile("E0")
print list[1]