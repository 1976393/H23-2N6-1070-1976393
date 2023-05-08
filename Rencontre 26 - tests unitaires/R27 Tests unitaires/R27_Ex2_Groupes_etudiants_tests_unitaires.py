import R27_Ex2_Groupes_etudiants as Ge
import unittest
from constant import *

class Test_ajouter_etudiant(unittest.TestCase):

    def test_ajouter_1_etudiant_depasse_max(self):
       # Instanciez 3 étudiants
       # Instanciez un groupe avec une liste de 3 etudiants
       # Instanciez un autre étudiant
       # Vérifiez que vous obtenez une erreur quand vous testez l'ajout de cet autre étudiant
       étudiant1 = Ge.Etudiant(1,1,1)
       étudiant2 = Ge.Etudiant(1,1,1)
       étudiant3 = Ge.Etudiant(1,1,1)
       groupe1 = Ge.Groupe([])
       groupe1.ajouter_etudiant(étudiant1)
       groupe1.ajouter_etudiant(étudiant2)
       groupe1.ajouter_etudiant(étudiant3)
       étudiant4 = Ge.Etudiant(1,1,1)
       with self.assertRaises(expected_exception=Exception):
           groupe1.ajouter_etudiant(étudiant4)
                                
    def test_ajouter_1_etudiant_ok(self):
        # Instanciez un etudiant
        # Instanciez un groupe avec cet etudiant
        # Instanciez un autre étudiant
        # Testez l'ajout de cet autre étudiant
        # Vérifiez que le dernier étudiant du groupe est celui que vous avez ajouté
        # Vérifiez que le nombre d'étudiants du groupe est maintenant de 2
       étudiant1 = Ge.Etudiant(1976393,1,1)
       groupe1 = Ge.Groupe([])
       groupe1.ajouter_etudiant(étudiant1)
       étudiant2 = Ge.Etudiant(1976394,1,1)
       groupe1.ajouter_etudiant(étudiant2)
       self.assertEqual(len(groupe1.ls_etudiants)-1,groupe1.ls_etudiants.index(étudiant2))
       self.assertEqual(2,len(groupe1.ls_etudiants))




if __name__ == '__main__':
    unittest.main(verbosity=2)