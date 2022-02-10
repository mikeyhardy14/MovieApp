# Done: 
# This is the file to prompt the user if he likes movies. The user can respond
# with Yes/No/Not Seen. 
# Link to UI
# To Do:
# Link Algorithm
# Fix Invalid answer new movie problem
import csvfilter
import filter



def welcome():
    print("Welcome to the Mission 100 MovieApp Review application! \n\nLet's get started. Respond to the following questions by saying 'Yes' 'No' or 'Not Seen'\n")

 
def question():
    movie=csvfilter.new_movie()
    title = movie[1]
    i= input("Did you like: {}? ".format(title))

    if i =="Yes":
        print("Great Movie!")
        #add to new csv file "likedmovies.csv"
        filter.likedmovie(movie)
            
    elif i =="No":
        print("Bold Take!")
        #add to new file "dislikedmovies.csv"
        filter.dislikedmovie(movie)
    elif i == "Not Seen":
        print("You're missing Out!")
    else:
        print("That is not a valid answer. Be sure to capitalize the proper letters.")