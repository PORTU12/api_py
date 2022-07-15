# Le joueur dépose un montant initial pour commencer à jouer. Il devine un chiffre entre 1 et 10 et saisit le montant 
# de sa mise. S'il gagne, il recevra 10 fois l'argent qu'il a misé. S'il parie sur un mauvais numéro, il perd le
# montant de sa mise. Le jeu continue jusqu'à ce que l'utilisateur veuille jouer

#import module;
#from 
import random
import numpy


player = ["ramen", "youki", "magond", "pieuvre", "boule"]
proba = [0.1, 0.4, 0.5, 0.3, 0.2]

#Afficher un nom au hasard
#player_name = random.choices(player, k=3)
#print(player_name[0], player_name[1], player_name[2])
print(numpy.random.choice(player, 3, p = proba))