from cache import LRUCache
from node import Node 
from doublylinkedlist import DoublyLinkedList
import csv

class CarModelFinder:

    def __init__(self, ipt="Acura", year="2024"):
        self.ipt = ipt
        self.year = year

    def find(self):
        string = "Cars of Model: \n"
        car_cache = LRUCache()
        make = car_cache.search(self.ipt)
        try:
            with open("models2024.csv") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for row in reader:
                    if row[1] == make:
                        string += str(row[2]) + "\n"
            return string
        except:
            return "ERROR: Car models for car make not found"
        
    def getInput(self):
        return self.ipt
    
    def setInput(self, provided):
        self.ipt = provided

    def getYear(self):
        return self.year
    
    def setInput(self, provided):
        self.year = provided
    
while True:
    prompt = input("Enter desired car make: ")
    cmf = CarModelFinder(prompt)
    print(cmf.find())