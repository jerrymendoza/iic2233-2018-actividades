import csv
from collections import namedtuple

PATH="MiniDatabase/"


def load(path):
    with open(path, newline="") as infile:
        reader = csv.reader(infile,skipinitialspace=True)
        Data = namedtuple("Data", next(reader))
        for row in reader:
            yield Data(*row)

#for i in leer("MiniDatabase/actors.csv"):
#    print(i)

#lista=["1","hola","2.7/10", "83%", "51/100", "$504.815.761"]
#print(list(map(lambda x: int(x) if x.isdigit() else x ,lista)))

def load_database():
    with open(PATH+"movies.csv", newline="") as file:
        reader = csv.reader(file,skipinitialspace=True)
        Data = namedtuple("Data", next(reader))
        to_int = lambda x: int(x) if x.isdigit() else x 
        for row in reader:
            yield Data(*list(map(to_int,row)))
            

