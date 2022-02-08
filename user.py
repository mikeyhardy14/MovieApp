# Done: 
# This is the file to prompt the user if he likes movies. The user can respond
# with Yes/No/Not Seen. 
# Link to UI
# To Do:
# Link Algorithm
# Fix Invalid answer new movie problem
import csvfilter
import csv



def welcome():
    print("Welcome to the Mission 100 MovieApp Review application! \n\nLet's get started. Respond to the following questions by saying 'Yes' 'No' or 'Not Seen'\n")

    
# def answer(x):
#     if x =="Yes":
#         print("Great Movie!")
#         #add to new csv file "likedmovies.csv"
#         #with open ('likedmovies.csv', 'w') as csvfile:
#         #    fieldnames = ['movie number']
#         #    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
#         #    writer.writerow({'movienumber': movie[0]})
            
#     elif x =="No":
#         print("Bold Take!")
#         #add to new file "dislikedmovies.csv"
#                 #with open ('dislikedmovies.csv', 'w') as csvfile:
#         #    fieldnames = ['movie number']
#         #    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
#         #    writer.writerow({'movienumber': movie[0]})
#     elif x == "Not Seen":
#         print("You're missing Out!")
#         #add to new file "already_asked"
#         #with open ('already_existed.csv', 'w') as csvfile:
#         #    fieldnames = ['movie number']
#         #    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
#         #    writer.writerow({'movienumber': movie[0]})
#     else:
#         print("That is not a valid answer. Be sure to capitalize the proper letters.")

def question():
    movie=csvfilter.new_movie()
    title = movie[1]

    #Metascore =int(moviedict[13])
    #def actors
    #def MultGenre:

    i= input("Did you like: {}? ".format(title))
#    answer(i)

    if i =="Yes":
            print("Great Movie!")
        #add to new csv file "likedmovies.csv"
        #with open ('likedmovies.csv', 'w') as csvfile:
        #    fieldnames = ['movie number']
        #    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
        #    writer.writerow({'movienumber': movie[0]})
            
    elif i =="No":
        print("Bold Take!")
        #add to new file "dislikedmovies.csv"
                #with open ('dislikedmovies.csv', 'w') as csvfile:
        #    fieldnames = ['movie number']
        #    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
        #    writer.writerow({'movienumber': movie[0]})
    elif i == "Not Seen":
        print("You're missing Out!")
        #add to new file "already_asked"
        #with open ('already_existed.csv', 'w') as csvfile:
        #    fieldnames = ['movie number']
        #    writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
        #    writer.writerow({'movienumber': movie[0]})
    else:
        print("That is not a valid answer. Be sure to capitalize the proper letters.")