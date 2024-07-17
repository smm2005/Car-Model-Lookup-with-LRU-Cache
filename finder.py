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
            return "ERROR: Cars not found"
    
cmf = CarModelFinder()
print(cmf.find())