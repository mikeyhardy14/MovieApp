import random
import genre

d_tally=0
big_num=0
total = 0
fin=0
g_tally=0
p_tally=0



def algorithm(imdbrat):
  #variables
  genre = 1.6 *g_tally
  rating = 1.4 *imdbrat
  
  total = (genre + rating)
  if (big_num < total):
    fin =total
    
big_num= fin
