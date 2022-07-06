age = int(input("your are miss : "));

while True:
    try:
        age = int(input('Please enter your age:'))
    except ValueError:
        print('Sorry, I do not understand that')
    else:
        break
if (age >= 18):
    print("you are able to vote")
else:
    print("you are not able to vote")

livre = "beloved"
livre = 0
nouveau_livre = "Gatsby le Magnifique"
livre = livre +1

print(livre)

liste_nombres = [1, 6, 98, 52, 1045, 3]

# 1) classez la liste
liste_nombres.sort()
# 2) supprimez le premier élément de la liste
liste_nombres.pop(0)
# 3) ajoutez le nombre "1097" à la fin de la liste
liste_nombres.append(1097)
# 4) récupérez le deuxième élément dans une variable "deuxieme_element"
deuxieme_element = liste_nombres[1]
print(deuxieme_element) # la console devrait afficher "6" !

# 5) affichez la longueur de la liste
print(len(liste_nombres))

# 1) Créez une variable de type dictionnaire appelée "chaussure"
chaussure = dict()
chaussure["taille"] = 42
chaussure["marque"] = "Nike"
chaussure["race"] = "berger-allemand"


""" 2) Ajoutez les éléments suivants dans le dictionnaire :
   - clef "taille" avec la valeur 42
   - clef "marque" avec la valeur "Nike"
   - clef "race" avec la valeur "berger-allemand"
"""

# 3) On s'est trompés ! Supprimez la clef "race" du dictionnaire :)
chaussure.pop('race')
# 4) Récupérez la taille de la chaussure dans une variable appelée "taille"
taille = chaussure['taille']
print(f"La taille de la chaussure est {taille}")  # 42 normalement !


# 1) Comprenez le code ci-dessous
a = 3
b = 7
c = 5

vrai_ou_faux = (a < b or b != c) and c >= b

# 2) Déduisez-en la valeur de vrai_ou_faux et assignez la dans la variable nommée "solution"
solution = False

# 3) Vérifiez votre intuition en faisant tourner le code (> "Run")
print(f"{solution} est la bonne valeur de vrai_ou_faux !" if solution == vrai_ou_faux else "Raté")


# 1) Comprenez le code ci-dessous
a = True
b = False
c = True

if a and b:
    x = 5
elif not c:
    x = 4
elif a:
    x = 8
else:
    x = 7

# 2) Déduisez-en la valeur de x et assignez la dans la variable nommée "solution"
solution = 8

# 3) Vérifiez votre intuition en faisant tourner le code (> "Run")
print(f"{solution} est la bonne valeur de x !" if solution == x else "Raté")


"""
Le but de l'exercice est de calculer la somme des 100 premiers entiers naturels !

Pour information : 
vous êtes sur les pas du célèbre mathématicien Gauss
https://fr.wikipedia.org/wiki/Somme_(arithm%C3%A9tique)
"""

# 1) Utilisez une boucle et la fonction "range" pour calculer la somme.
# Testez et récupérez le résultat en faisant tourner le code (> "Run")
x = 0
for x in range(x, 100):
    x = x+1
    print("la somme de x : ", x)
# 2) Assignez le résultat obtenu dans la variable "solution" pour vérification
solution = 5

# Ne touchez pas le print ci-dessous :)
print(f"{solution} est la bonne valeur de la somme !" if solution == (100 * 101) / 2 else "Raté")

# Vous allez créer une fonction permettant de calculer le produit d'une liste de nombres

# Ecrivez la fonction et testez avec le bouton > "Run" que le calcul est correct !
def produit_entiers(liste_entiers):
    # écrivez le code ici

# Ne touchez pas le code de vérification ci-dessous :)
assert 1 == produit_entiers([1, 1, 1])
assert 6 == produit_entiers([1, 2, 3])
assert 0 == produit_entiers([1, 2, 3, 90, 0])
