import csv
from collections import namedtuple

PATH = "MiniDatabase/"
files = ["actors.csv", "genres.csv", "movies.csv", "reviews.csv"]


def load(path):
    with open(path, newline="") as infile:
        reader = csv.reader(infile, skipinitialspace=True)
        Data = namedtuple("Data", next(reader))
        to_int = lambda x: int(x) if x.isdigit() else x
        for row in reader:
            yield Data(*list(map(to_int, row)))

# for i in leer("MiniDatabase/actors.csv"):
#    print(i)

#lista = ["1", "hola", "2.7/10", "83%", "51/100", "$504.815.761"]
#print(list(map(lambda x: int(x) if x.isdigit() else x ,lista)))


def load_database():
    with open(PATH + files[2], newline="") as file:
        reader = csv.reader(file, skipinitialspace=True)
        Data = namedtuple("Data", next(reader))
        to_int = lambda x: int(x) if x.isdigit() else x
        for row in reader:
            yield Data(*list(map(to_int, row)))


#filter_by_date(generator, int, bool)
def filter_by_date(movies, date, lower=True):
    if lower:
        return filter(lambda x:isinstance(x.date,int) and x.date<date,movies)
    else:
        return filter(lambda x:isinstance(x.date,int) and x.date>date,movies)


#popular_movies(generator,int, int, str)
def popular_movies(movies, r_min, r_max, r_type="All"):
    pass

#best_comments(generator, int)
def best_comments(movies, n):
    pass


if __name__ == "__main__":
    print(type(filter_by_date(load_database(), 2008)))

    for i in filter_by_date(load_database(), 2008):
        print(i)
