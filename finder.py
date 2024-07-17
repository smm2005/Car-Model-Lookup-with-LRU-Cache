from cache import LRUCache
from node import Node
from doublylinkedlist import DoublyLinkedList
import csv

class CarModelFinder:

    def __init__(self, ipt="Acura"):
        self.ipt = ipt

    def find(self):
        string = "Cars of Model: \n"
        car_cache = LRUCache()
        car_cache.search(self.ipt)
        try:
            with open("models2024.csv") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for row in reader:
                    if row[1] == self.ipt:
                        string += str(row[2]) + "\n"
            return string
        except:
            return "ERROR: Car models for car make not found"
        
    def getInput(self):
        return self.ipt
    
    def setInput(self, provided):
        self.ipt = provided
    
prompt = input("Enter desired car make: ")
cmf = CarModelFinder()
if prompt != "":
    cmf.setInput(prompt)
print(cmf.find())