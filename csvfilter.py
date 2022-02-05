import csv
from platform import release
import random
from random import choice
from turtle import title
from unicodedata import name
#import pandas as pd



moviedict = {}

# open file and convert to dictionary
with open('IMDB_Top250Engmovies2_OMDB_Detailed.csv') as f:
    reader = csv.reader(f)
    moviedict = random.choice(list(reader))
    
title = moviedict[1]
Moiveyear = moviedict[2]
rated = moviedict[3]
released = moviedict[4]
director =moviedict[6]
writer = moviedict[7]
plot = moviedict[9]
Awards = moviedict[11]
ratings = float(moviedict[12])
Metascore =int(moviedict[13])
TomatoUrl = moviedict[17]
Production = moviedict[18]



#def actors
#def MultGenre:
    
