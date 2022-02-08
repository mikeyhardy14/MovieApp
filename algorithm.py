from collections import Counter
import re
#IMDB_Top250Engmovies2_OMDB_Detailed.csv
#likemovies.csv

def count_word(file_name):
        with open(file_name) as f:
          return Counter(f.read().split()).most_common(3)

print("Frequency :",count_word("likemovies.csv"))