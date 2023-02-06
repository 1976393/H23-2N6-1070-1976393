# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


nom_fichier = "Étudiants gr1010"
exercice_sep = "___________________________________"

# Faites le code demandé, en imprimant toujours exercice_sep après chaque partie de cet exercice


#  Vous savez que le groupe est toujours les 4 derniers caractères du nom de fichier#
# Q1 Faites le code nécessaire pour obtenir ces 4 derniers caractères en utilisant le slicing à partir de la fin #
groupe = nom_fichier[-4:]
print(groupe)
print(exercice_sep)

str_joie = "Joie"
# Q2 Imprimez chacun des caractères de la variable str_joie en utilisant for, len et range #
for i in range(len(str_joie)):
    print(str_joie[i])
print(exercice_sep)

    
# Q3 Imprimez chacun des caractères de la variable str_joie de façon INVERSÉE en utilisant for, len et range et un indice #
# que vous modifierez dans la boucle for#
ind_i = -1
for i in range(len(str_joie)):
    print(str_joie[ind_i]) 
    ind_i -= 1   
print(exercice_sep)  


# Q4 Vérifiez si le mot un_mot est un palindrome  
# Vous pouvez commencer par inverser un_mot dans un_autre_mot
# Puis comparez les deux mots
# Faites ensuite la structure if...else... pour afficher les messages suivants:
#    Si la condition est vraie, affichez un message comme quoi le mot est un palindrome
#    Si la contition est fausse, affichez un message comme quoi le mot trouvé n'est pas un palindrom

# Ainsi, avec le mot "kayak" le résultat attendu est "Le mot kayak est un palindrome"
un_mot = "kayak"
ind_i = -1
un_autre_mot = ""
for i in range(len(un_mot)):
    un_autre_mot += un_mot[ind_i]
    ind_i -= 1   

if un_mot == un_autre_mot:
    print(f"Le mot {un_mot} est un palindrome")
else:
    print(f"Le mot {un_mot} n'est pas un palindrome")
print(exercice_sep)  

# Changez la question précédente pour obtenir un mot de l'usager 
# Faire en sorte que ce code fonctionne en boucle tant que le mot entré n'est pas stop #
mot_input = ""
while (not mot_input == "stop"):
    mot_input = input("Entrez un mot: " )
    ind_i = -1
    un_autre_mot = ""
    for i in range(len(mot_input)):
        un_autre_mot += mot_input[ind_i]
        ind_i -= 1   

    if mot_input == un_autre_mot:
        print(f"Le mot {mot_input} est un palindrome")
    else:
     print(f"Le mot {mot_input} n'est pas un palindrome")
     
print(exercice_sep)  

