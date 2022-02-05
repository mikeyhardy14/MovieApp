import csv
import random
from random import choice
#import pandas as pd



moviedict = {}

# open file and convert to dictionary
with open('IMDB_Top250Engmovies2_OMDB_Detailed.csv') as f:
    reader = csv.reader(f)
    moviedict = random.choice(list(reader))
    
print(moviedict)