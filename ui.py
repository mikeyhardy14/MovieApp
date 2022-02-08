import user
import csv
import csvfilter

    
def response(x):
    if x =="Yes":
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
    print("Our movie recommendation is: '",title,"' from '",movieyear,"'. Here is the plot:\n\n",plot,"\n\n")
    i=input("Are you happy with your recommendation?")
    response(i)

def q_loop():
    n =0
    while(n < 10):
        user.question()
        n += 1
    print("The results are in!\n")
    recommend()
    
user.welcome()
q_loop()



