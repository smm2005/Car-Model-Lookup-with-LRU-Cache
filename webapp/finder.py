from cache import LRUCache
from node import Node 
from doublylinkedlist import DoublyLinkedList
import csv

class CarModelFinder:

    car_cache = LRUCache()
    csv_cache = LRUCache(c=5)
    string = ""

    def __init__(self, ipt="Acura", year="2024"):
        self.ipt = ipt
        self.year = year

    def find(self):
        make = self.car_cache.search(self.ipt)
        func = self.csv_cache.search("self.load(\"models{}.csv\", \"{}\")".format(str(self.year), make))
        try:
            exec(func)
            if self.string == "":
                self.string = "CARS NOT FOUND"
        except:
            self.string = "CARS NOT FOUND"
        
    def load(self, file, car_make):
        with open("webapp/models/"+file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                if row[1] == car_make:
                    self.string += "&nbsp;&nbsp;"+ str(row[2]) + "<hr>"
        
    def getInput(self):
        return self.ipt
    
    def setInput(self, provided):
        self.ipt = provided

    def getYear(self):
        return self.year
    
    def setYear(self, provided):
        self.year = provided

    def getString(self):
        return self.string
