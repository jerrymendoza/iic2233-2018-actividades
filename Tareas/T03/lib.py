import csv
from collections import namedtuple

PATH = "MiniDatabase/"
files = ["actors.csv", "genres.csv", "movies.csv", "reviews.csv"]

def imdb(rating_str):
    if rating_str != "N/A":
        return float(rating_str.split("/")[0])
    else:
        return "N/A"

def rt(rating_str):
    if rating_str!= "N/A":
        return int(rating_str.split("%")[0])
    else:
        return "N/A"
def metacritic(rating_str):
    if rating_str != "N/A":
        return int(rating_str.split("/")[0])
    else:
        return "N/A"



def _convertir_tipo(data):
    data = data._replace(rating_imdb=imdb(data.rating_imdb))
    data= data._replace(rating_rt=rt(data.rating_rt))
    data= data._replace(rating_metacritic=metacritic(data.rating_metacritic))
    return data


#def load(path):
#    with open(path, newline="") as infile:
#        reader = csv.reader(infile, skipinitialspace=True)
#        Data = namedtuple("Data", next(reader))
#        to_int = lambda x: int(x) if x.isdigit() else x
#        for row in reader:
#            yield Data(*list(map(to_int, row)))

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
    #convertir_tipo
    movies_int=map(_convertir_tipo,movies)
    return 



#best_comments(generator, int)
def best_comments(movies, n):
    pass


if __name__ == "__main__":
    print(type(filter_by_date(load_database(), 2008)))

    for i in filter_by_date(load_database(), 2008):
        print(i)
    for i in popular_movies(load_database(),1,1):
        print(i)