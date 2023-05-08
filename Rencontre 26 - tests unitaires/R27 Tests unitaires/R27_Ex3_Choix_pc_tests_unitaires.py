from cgitb import text
import R27_Ex3_Choix_pc as Cpc
import unittest
from constant import *

# Dans le programme, la sélection des composantes est effectué à travers l'interface graphique.
# On ne peux pas faire cela lors des tests
# On devra donc utilisé la méthode .set(value="valeur qu'on veut mettre") pour changer la valeur dans notre code.

# documentation de customtkinter : https://customtkinter.tomschimansky.com/documentation/widgets/combobox

class Test_estimer(unittest.TestCase):

    def test_estimer_sans_processeur(self):
        # Instanciez la classe Choix

        # Testez que le choix du processeur est   "Choisis ton processeur    "

        #           faites l'appel de la méthode estimer()

        # Vérifier que le texte du lbl_message est égal à "Tu dois choisir un processeur"

        choix = Cpc.Choix()
        choix.estimer()
        self.assertEqual("Tu dois choisir un processeur.",choix.lbl_message.cget("text"))
        

    def test_estimer_sans_carte_graphique(self):
        # Cette fois-ci donnez un choix valide pour le processeur
        choix = Cpc.Choix()
        choix.choix_processeur.set("AMD Ryzen 9 5950X")
        choix.estimer()
        self.assertEqual("Tu dois choisir une carte graphique.",choix.lbl_message.cget("text"))

    def test_estimer_sans_RAM(self):
        # Cette fois-ci donnez un choix valide pour le processeur et pour la carte graphique
        choix = Cpc.Choix()
        choix.choix_processeur.set("AMD Ryzen 9 5950X")
        choix.choix_carte_graphique.set("GeForce RTX 3090Ti")
        choix.estimer()
        self.assertEqual("Tu dois choisir une barrette RAM.",choix.lbl_message.cget("text"))

    def test_estimer_les_3_choix(self):
        # Instanciez la classe Choix
        choix = Cpc.Choix()
        # donner le choix de processeur "AMD Ryzen 9 5950X         "
        choix.choix_processeur.set("AMD Ryzen 9 5950X         ")
        # donner le choix de carte graphique "GeForce RTX 3090Ti        "
        choix.choix_carte_graphique.set("GeForce RTX 3090Ti        ")
        # donner le choix de barrette RAM  "G.SKILL Trident Z5        "
        choix.choix_RAM.set("G.SKILL Trident Z5        ")
        #        appeler la méthode estimer()
        choix.estimer()
        # Vérifier que le texte du lbl_message est égal à "Pour tes choix, l'estimé est de 3720.26$."
        self.assertEqual("Pour tes choix, l'estimé est de 3720.26$.",choix.lbl_message.cget("text"))
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)