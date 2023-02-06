# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


exercice_sep = "___________________________________"
# Faites le code demandé, en imprimant toujours exercice_sep après chaque partie de cet exercice


salutation = "Bonjour"
# Q1 Imprimez chacun des caractères de la variable salutation en utilisant for, len et range #
for i in range(len(salutation)):
    print(salutation[i])
print(exercice_sep)

    
# Q2 Demandez à l'usager d'entrer un chiffre pair en boucle
# Si le chiffre entré est pair, affichez "Merci vous avez entré le chiffre X, soit un chiffre pair."  où X est le chiffre entré
# Si l'usager entre un chiffre impair vous sortez de la boucle et affichez "Non, vous avez entré le chiffre X, et ce n'est pas un chiffre pair." #
nb_input = 2
estPair = nb_input % 2 == 0;
while (estPair):
    nb_input = int(input("Entrez un nombre entier: " ))
    estPair = nb_input % 2 == 0; 
    if estPair:
        print(f"Merci vous avez entré le chiffre {nb_input} , soit un chiffre pair. ")
    else:
     print(f"Non, vous avez entré le chiffre {nb_input}, et ce n'est pas un chiffre pair.")
     
print(exercice_sep)    



