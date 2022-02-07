# Done: 
# This is the file to prompt the user if he likes movies. The user can respond
# with Yes/No/Not Seen. 
# To Do:
# Link Algorithm
# Link to UI
# Fix Invalid answer new movie problem
import csvfilter



def welcome():
    print("Welcome to the Mission 100 MovieApp Review application! \n\n\nLet's get started. Respond to the following questions by saying 'Yes' 'No' or 'Not Seen'\n")

    
def answer(x):
    if x =="Yes":
        print("Great Movie!")
        #add to new csv file "likedmovies.csv"
    elif x =="No":
        print("Bold Take!")
        #add to new file "dislikedmovies.csv"
    elif x == "Not Seen":
        print("You're missing Out!")
        #add to new file "movienotseen.csv"
    else:
        print("That is not a valid answer. Be sure to capitalize the proper letters")

def question():
    movie=csvfilter.new_movie()
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
    #Metascore =int(moviedict[13])
    #def actors
    #def MultGenre:

    i= input("Did you like: {}? ".format(title))
    answer(i)

