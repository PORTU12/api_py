
import string


fruit_prix = 100
customer_name = input("Entrez votre nom : ")
customer_name = customer_name.isupper();
customer_fruit = int(input("Combien de fruits voulez-vous ? : "))
customer_money = input("Combien avez-vous ? : ")

cout_achat = fruit_prix * customer_fruit;

resultat = customer_money - cout_achat;