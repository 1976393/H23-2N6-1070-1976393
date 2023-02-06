# Il n'y a pas de questions dans ce fichier.
# Il s'agit de petites fonctions pour les exercices.
import time, random

def annee_de_naissance(age):
    return (f"Année de naissance : {(time.localtime()[0] - (age)-1)} ou {time.localtime()[0]-int(age)}")


def generation_variable():
    var2 = True
    var4 = "6"
    var5 = "int"
    var6 = ["str","float"]
    var7 = ["str"]
    var8 = 1 / 1
    return [var6,var7,var4,var2,var8,var5]


def generateur_100_noms():
    with open("noms_employées", "r") as fichier:
        lignes = fichier.readlines()
        liste_good = list()
        for nom in lignes:
            liste_good.append(f"{nom[:-1]}\n")
        print(liste_good)
        
def type_aleatoire():
    des = random.randomint(0,1)
    match des:
        case 0 : return int()
        case 1 : return str()


liste_employes= ['01 Ellen Ferguson\\n', '02 Essie Powell\\n', '03 Donald Berry\\n', '04 Lucile Rogers\\n', '05 Verna Wells\\n', '06 Nell Harris\\n', '07 Rosie Figueroa\\n', '08 Philip Dean\\n', '09 Linnie Greene\\n', '10 Manuel Cobb\\n', '11 Nettie Romero\\n', '12 Lelia Buchanan\\n', '13 Noah Hines\\n', '14 Matthew Patterson\\n', '15 Isaac Craig\\n', '16 Winnie Fowler\\n', '17 Lenora Chambers\\n', '18 Eva Flores\\n', '19 Alexander Rogers\\n', '20 Todd Vasquez\\n', '21 Luke Gomez\\n', '22 Patrick Greene\\n', '23 Scott Watkins\\n', '24 Blanche Rivera\\n', '25 Gregory Abbott\\n', '26 Anne Reid\\n', '27 Richard Strickland\\n', '28 Alta Reese\\n', '29 Ola Rodriquez\\n', '30 Janie Padilla\\n', '31 Miguel Pearson\\n', '32 Bobby Davis\\n', '33 Georgie Moody\\n', '34 Ethel Hicks\\n', '35 Michael Harvey\\n', '36 Zachary Carr\\n', '37 Roger Banks\\n', '38 Louise Wolfe\\n', '39 Walter Butler\\n', '40 Jayden Williams\\n', '41 Roy Christensen\\n', '42 Adrian Alvarez\\n', '43 Corey James\\n', '44 Margaret Hodges\\n', '45 Curtis Carson\\n', '46 Jeffery Zimmerman\\n', '47 Gene Frank\\n', '48 Bess Diaz\\n', '49 Jon Terry\\n', '50 Steven Waters\\n', '51 Bernard James\\n', '52 Isabel Daniel\\n', '53 Janie Holmes\\n', '54 Joe Sparks\\n', '55 Hallie Owen\\n', '56 Nettie Hudson\\n', '57 Ora Mendoza\\n', '58 Lucile Walsh\\n', '59 Roger Morrison\\n', '60 Barbara Gray\\n', '61 Mary Watkins\\n', '62 Jennie Robbins\\n', '63 John Moss\\n', '64 Lillian Guerrero\\n', '65 Warren Hudson\\n', '66 Kathryn Becker\\n', '67 Oscar Wright\\n', '68 Jordan Wise\\n', '69 Ida Hall\\n', '70 Roxie Russell\\n', '71 Angel Conner\\n', '72 Stephen Newman\\n', '73 Leo Webster\\n', '74 Cecilia Bennett\\n', '75 Travis Sims\\n', '76 Millie Nelson\\n', '77 Abbie Chambers\\n', '78 Mario Swanson\\n', '79 Herbert Russell\\n', '80 Cameron Robertson\\n', '81 Tom Flowers\\n', '82 Henrietta Mills\\n', '83 Hunter Bridges\\n', '84 Glenn Barber\\n', '85 Connor Vaughn\\n', '86 Ellen Lloyd\\n', '87 Kyle West\\n', '88 Sarah Bush\\n', '89 Marvin Alexander\\n', '90 Carrie Dawson\\n', '91 Austin Maldonado\\n', '92 Vernon Higgins\\n', '93 Cornelia Brooks\\n', '94 Millie Luna\\n', '95 Gordon Olson\\n', '96 Ann Morton\\n', '97 Andre Figueroa\\n', '98 Albert Walsh\\n', '99 Elijah Summers\\n', '00 Essie Morton\\n']