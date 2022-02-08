import csv
import random

moviedict = {}

# open file and convert to dictionary 
def new_movie():
    with open('IMDB_Top250Engmovies2_OMDB_Detailed.csv') as f:
        reader = csv.reader(f)
        moviedict = random.choice(list(reader))
    #return movie selection
    return moviedict


