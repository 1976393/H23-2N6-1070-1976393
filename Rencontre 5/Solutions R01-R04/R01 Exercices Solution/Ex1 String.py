
# Créez 3 amies (amie1, amie2, amie3) et donnez leur des prénoms différents (et différents de mes amies à moi) #
amie1 = 'Sophie'
amie2 = 'Laurence'
amie3 = 'Wissale'
# Pour l'amie1, affichez dans la console les 3 premières lettres de son prénom #
print(amie1[0:3])
# Pour l'amie2, affichez dans la console le nombre de lettres qu'il y a dans son nom #
print(len(amie2))
# Créez une variable appelée salutation avec la valeur 'Bonne année'  #
salutation = 'Bonne année'
# Affichez dans la console un message pour souhaiter 'Bonne année' à vos trois amies, en utilisant salutation et leurs prénoms et en utilisant f' #
message1 = f'{salutation} {amie1}! {salutation} {amie2}! {salutation} {amie3}!'
print(message1)
# Affichez dans la console un message pour souhaiter 'BONNE ANNÉE' à vos trois amies, en utilisant salutation et upper(), avec leurs prénoms et en utilisant f' #
message2 = f'{salutation.upper()} {amie1}! {salutation.upper()} {amie2}! {salutation.upper()} {amie3}!' 
print(message2) 
# Affichez dans la console la dernière lettre du prénom de votre troisième amie' #
print(amie3[-1])
