import csv
from csv import writer
import csvfilter

movie= csvfilter.testmovie()

def likedmovie(movie):
    with open ('likemovies.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([movie])
        
def dislikedmovie(movie):
    with open ('dislikemovies.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow([movie])
        f.close()        
        