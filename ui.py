import user
import csvfilter
import os

    
def response(x):
    if x =="Yes":
        if (os.path.exists('likemovies.csv') and os.path.isfile('likemovies.csv')):
            os.remove('likemovies.csv')
        if (os.path.exists('dislikemovies.csv') and os.path.isfile('dislikemovies.csv')):
            os.remove('dislikemovies.csv')
        print("Thank you for using MovieApp")
        
    elif x =="No":
        print("BOOOOOOOOO!!!!!!!!!!!!!!......Let's try this again.")
        q_loop()
    else:
        print("INVALID RESPONSE!")
  
def recommend():
    print("MovieApp has a recommendation!\n\n")
    movie = csvfilter.new_movie()
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
    print("Our movie recommendation is: '",title,"' from '",movieyear,"'. Here is the plot:\n",plot,"\n")
    i=input("Are you happy with your recommendation?\n")
    response(i)

def q_loop():
    n =0
    while(n < 10):
        user.question()
        n += 1
    print("The results are in!\n")
    recommend()
    
def start():   
    user.welcome()
    q_loop()

start()


