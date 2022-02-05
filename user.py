from tkinter import N
from urllib import response
import csvfilter

movie=csvfilter.moviedict

title = movie[1]
movieyear = movie[2]
rated = movie[3]
released = movie[4]
director =movie[6]
writer = movie[7]
plot = movie[9]
awards = movie[11]
ratings = float(movie[12])
tomatoUrl = movie[17]
production = movie[18]


def answer(x):
    if x =="Yes":
        print("Nice!")
        #add number for algorithm
    elif x =="No":
        print("You suck")
        #subtract number for algorithm
    else:
        print("You're missing Out!")

print("Welcome to the Mission 100 MovieApp Review application! \nLet's get started. Respond to the following questions by saying 'Yes' 'No' or 'Not Seen'")
i= input("Did you like: {}?\n".format(title))

answer(i)