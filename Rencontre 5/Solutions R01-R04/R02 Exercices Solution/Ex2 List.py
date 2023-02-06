# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' de séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées             # 


# Q1                                                                                                                   #
# Créez une liste de 3 barrettes de RAM parmis les suivantes:                                                          #
#          G.SKILL Trident Z5, CORSAIR Dominator, CORSAIR Vengeance, G.SKILL Ripjaws V, G.SKILL Ripjaws X              #
# imprimez la liste                                                                                                    #
barrettes_ram = ['CORSAIR Dominator', 'CORSAIR Vengeance', 'G.SKILL Ripjaws V']
print(f"Q1: Voici la liste: {barrettes_ram}")
print(80*'_' )


# Q2                                                                                                                   #
# Ajoutez un item à la fin de la liste avec append                                                                     #
# et affichez la dernière barrette RAM que vous avez dans la liste                                                     #
barrettes_ram.append('G.SKILL Ripjaws X')
print(f"Q2: Dernière barrette de la liste, récemment ajoutée avec append: {barrettes_ram[-1]}")
print(80*'_' )


#  Q3                                                                                                               #
#  Observez quelle est la deuxième barrette de RAM de votre liste                                                   #
#  Enlevez-la de la liste avec remove                                                                               #
#  Imprimez la liste en spécifiant la barrette de RAM enlevée                                                       #
barrettes_ram.remove( 'CORSAIR Vengeance')
print(f"Q3: J'ai enlevé la barrette de ram  'CORSAIR Vengeance' avec remove. La liste est maintenant:\n  {barrettes_ram}")
print(80*'_' )

# Q4                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
barrettes_ram.sort()
print(f"Q4: La liste en ordre croissant: {barrettes_ram}")
print(80*'_' ) 

# Q5                                                                                                             #
# Ordonner la liste en ordre décroissant avec la méthode sorted (qui crée une nouvelle liste)                    #
# et imprimez-la                                                                                                 
barrettes_ram_inverse=sorted(barrettes_ram, reverse=True)
print(f"Q5: La nouvelle liste en ordre décroissant: {barrettes_ram_inverse}")
print(80*'_' ) 

# Q6                                                                                                                 #
# Imprimez le nombre d'éléments qu'il y a dans votre liste présentement                                              #
print(f"Q6: La liste contient: {len(barrettes_ram)}  barrettes de RAM.")
print(80*'_')

# Q7                                                                                                                 #
# Imprimez une sous-liste des deux dernières barrettes RAMS de votre liste, en utilisant le slicing                  #
print(f"Q7: Les deux dernières barrettes de la liste sont: {barrettes_ram[-2:]}")
print(80*'_')

