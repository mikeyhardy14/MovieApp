import random
def algorithm():
  #variables
  total = 0
  decade = 1
  genre = 1.6
  rating = 1.4
  production = 2
  
  #asking user about randomly selected movies
  asked = 0
  usedmovies = []
  while asked is < 10:
    #using random import select a movie from imdb top 250
    thismovie = random.randint(0,250) #use this to get random movie in list
    if thismovie
    response = input("If you like this movie type 'y', if you dislike this movie type 'n', if you havent seen this movie type 'hs': ")
    #have a few other things due today, working on those rn, will get back to this when I have time
