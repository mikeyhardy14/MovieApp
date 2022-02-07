import random

d_tally=0
big_num=0
total = 0
fin=0
g_tally=0
p_tally=0

def algorithm():
  #variables
  decade = 1 *d_tally
  genre = 1.6 *g_tally
  rating = 1.4 
  production = 2 *p_tally
  
  total = (decade+ genre + rating+ production)
  if (big_num < total):
    fin =total
    
big_num= fin