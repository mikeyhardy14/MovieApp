import csv
from random import randint
import pandas as pd


x =[randint(1,250) for p in range(0,1)]

print(x)

# open file
with open('IMDB_Top250Engmovies2_OMDB_Detailed.csv', 'r') as f:
    reader = csv.reader(f[x])
    for x in reader:
        print(x)
