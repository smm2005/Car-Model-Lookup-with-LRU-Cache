from cache import LRUCache
from node import Node 
from doublylinkedlist import DoublyLinkedList
import csv
from time import perf_counter

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
        except:
           self.string = "ERROR: CARS NOT FOUND"
        
    def load(self, file, car_make):
        self.string = "Cars of Model: \n"
        with open("models/"+file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                if row[1] == car_make:
                    self.string += str(row[2]) + "\n"
        
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

start1 = perf_counter()
cmf1 = CarModelFinder("Audi", "2019")
cmf1.find()
end1 = perf_counter()
print(end1 - start1)

start2 = perf_counter()
cmf2 = CarModelFinder("BMW", "2022")
cmf3 = CarModelFinder("Chevrolet", "2021")
cmf2.find()
cmf3.find()
end2 = perf_counter()
print(end2 - start2)

start3 = perf_counter()
cmf4 = CarModelFinder("Dodge", "2024")
cmf5 = CarModelFinder("Alfa Romeo", "2024")
cmf6 = CarModelFinder()
cmf7 = CarModelFinder("Nissan", "2021")
cmf4.find()
cmf5.find()
cmf6.find()
cmf7.find()
print(cmf4.getString())
end3 = perf_counter()
print(end3 - start3)

