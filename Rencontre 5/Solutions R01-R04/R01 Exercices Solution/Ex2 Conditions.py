# RAPPEL12
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

exercice_sep = "___________________________________"
# Faites le code demandé, en imprimant toujours exercice_sep après chaque partie de cet exercice


# 
# Q1 Demandez à l'usager d'entrer un nombre entre 1 à 10 #
#    Faites une structure de code conditionnelle pour vérifier si le nombre entré est entre 1 et 10
#    Si oui, affichez "Exellent vous avez entré un nombre entre 1 et 10"
#    Sinon, affichez "Erreur, vous n'avez pas entré un nombre entre 1 et 10"
#    
nb_input = int(input("Entrez un nombre entre 1 et 10: " ))
if 1 <= nb_input <= 10:
    print("Exellent vous avez entré un nombre entre 1 et 10")
else:
    print("Erreur, vous n'avez pas entré un nombre entre 1 et 10")
print(exercice_sep)  

# Q2 Demandez à l'usager d'entrer un mot#
#    Faites un test pour vérifier si la longueur du mot entré est plus petit ou égal à 5
#    Si oui, affichez "Bien vous avez utilisé un mot de vocabulaire court"
#    Sinon, faites un autre test pour vérifier si la longueur du mot entré est entre 6 et 10
#          , affichez "Très bien, vous avez utilisé un mot de vocabulaire plus élaboré"
#    Sinon, (pas besoin de test mais dans ce cas la longueur du mot sera supérieure à 10)
#            affichez "Excellent, vous avez un vocabulaire élaboré"
mot_input = input("Entrez un mot de la longueur que vous voulez, entre 1 et 15 lettres:  " )
print(len(mot_input))
if 1 <= len(mot_input) <= 5:
    print("Bien vous avez utilisé un mot de vocabulaire court")
elif 6 <= len(mot_input) <= 10:
    print("Très bien, vous avez utilisé un mot de vocabulaire plus élaboré")
else:
    print("Excellent, vous avez vraiment un vocabulaire très élaboré")
print(exercice_sep) 

    
# Q3 Comme dans l'exercice précédent mais dans le message incluez le mot entré et la longueur du mot
# par exemple: si le mot entré est patato, le message affiché sera 
# "Bien, vous avez entré le mot 'patato', soit un mot de 6 lettres. \n Vous avez utilisé un mot de vocabulaire plus élaboré"
mot_input = input("Entrez un mot de la longueur que vous voulez, entre 1 et 15 lettres: " )
if 1 <= len(mot_input) <= 5:
    print(f"Bien, vous avez entré '{mot_input}', soit un mot de {len(mot_input)} lettres. \n Vous avez utilisé un mot de vocabulaire court")
elif 6 <= len(mot_input) <= 10:
    print(f"Très bien, vous avez entré '{mot_input}', soit un mot de {len(mot_input)} lettres. \n Vous avez utilisé un mot de vocabulaire plus élaboré")
else:
    print(f"Excellent, vous avez entré '{mot_input}', soit un mot de {len(mot_input)} lettres. \n Vous avez vraiment un vocabulaire très élaboré")
print(exercice_sep) 

