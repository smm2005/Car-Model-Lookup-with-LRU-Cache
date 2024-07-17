from cache import LRUCache
from node import Node 
from doublylinkedlist import DoublyLinkedList
import csv
import time

class CarModelFinder:

    car_cache = LRUCache()
    csv_cache = LRUCache(c=5)

    def __init__(self, ipt="Acura", year="2024"):
        self.ipt = ipt
        self.year = year

    def find(self):
        make = self.car_cache.search(self.ipt)
        func = self.csv_cache.search("self.load(\"models{}.csv\", \"{}\")".format(str(self.year), make))
        exec(func)
        
    def load(self, file, car_make):
        string = "Cars of Model: \n"
        with open("models/"+file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                if row[1] == car_make:
                    string += str(row[2]) + "\n"
        print(string)
        
    def getInput(self):
        return self.ipt
    
    def setInput(self, provided):
        self.ipt = provided

    def getYear(self):
        return self.year
    
    def setInput(self, provided):
        self.year = provided
    
cmf = CarModelFinder(year="2024")
cmf.find()