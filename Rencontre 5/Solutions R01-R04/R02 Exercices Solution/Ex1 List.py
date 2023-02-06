# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' de séparer les questions. 

# Q1                                                                                                            #
# créez une liste de 4 à 5 sports  et imprimez la liste                                                         #
sports = ['tennis', 'natation', 'soccer', 'ski alpin']
print(f"Q1: Voici la liste: {sports}")
print(80*'_' )

# Q2                                                                                                             #
# affichez le premier sport de votre liste                                                                       #
print(f"Q2: Premier sport de la liste: {sports[0]}")
print(80*'_' )

# Q3                                                                                                             #
# ajoutez un item à la fin de la liste avec append                                                               #
# et affichez le dernier sport que vous avez dans la liste                                                       #
sports.append('ski de fond')
print(f"Q3: Dernier sport de la liste, récemment ajouté: {sports[-1]}")
print(80*'_' )

# Q4 ajoutez un item après le 1er sport de votre liste avec insert                                                  #
#    créez une liste d'autres sports que vous n'avez jamais fait                                                    #
#    imprimez la liste telle qu'elle est rendue                                                                     # 
#    ajoutez votre autre liste de sports à la première liste avec extend                                            #
#    imprimez la liste telle qu'elle est rendue                                                                     # 
sports.insert(1, 'badminton')
autres_sports = ['escrime', 'équitation']
sports.extend(autres_sports)
print(f"Q4: La liste après extend: {sports}")
print(80*'_' )

#  Q5                                                                                                               #
#  Imprimez le nom d'un sport que vous enleverez ensuite de la liste                                                #
#  Enlevez un sport de la liste avec remove                                                                         #
#  Imprimez la liste et voyez que le sport que vous avez enlevé avec remove est bel et bien enlevé                  #
#  Enlever le dernier sport de la liste avec pop. Le sport enlevé est retourné par pop Affichez-le                  #
#  Imprimez la liste en spécifiant le sport enlevé et utilisant f-string                                            #
print("Sport que je compte enlever avec remove: ski alpin")
sports.remove('ski alpin')
sport_removed = sports.pop()
print(f"Q5: J'ai enlevé le sport {sport_removed} avec pop. La liste est maintenant:\n  {sports}")
print(80*'_' )

# Q6                                                                                                             #
# Utilisez une boucle for pour passer à travers chaque sport dans la liste avec une boucle for                   #
# et affichez le sport sur différentes lignes                                                                    #
print("Q6:")
for sport in sports:
    print(sport)
print(80*'_' )  
  
# Q7                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
sports.sort()
print(f"Q7: La liste en ordre croissant: {sports}")
print(80*'_' ) 

# # obtenir les sports et leurs index à partir de 1 au lieu de à partir de 0 #
# for index,sport in enumerate(sports, start=1):
#      print(index, sport)

# Q8                                                                                                                 #
# changez la liste en un string séparé par une virgule et affichez ce str                                            #
sports_str = ', '.join(sports)
print(f"Q8: La liste devenue un str: {sports_str}")
print(80*'_')

# Q9                                                                                                                 #
# Imprimez une sous-liste des deux premiers sports, en utilisant le slicing                                          #
print(f"Q9: Les deux premiers cours de la liste sont: {sports[:2]}")
print(80*'_')

