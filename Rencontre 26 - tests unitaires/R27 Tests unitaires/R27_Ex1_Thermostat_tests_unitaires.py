import R27_Ex1_Thermostat as Ths
import unittest
from constant import *

class Test_initialisation(unittest.TestCase):

    def test_temperature_initial(self):
        nouveau_thermostat = Ths.Thermostat()
        self.assertEqual(nouveau_thermostat._temperature, TEMPERATURE_INITIALE)

    def test_initialisation_temperature_trop_elevee(self):
        with self.assertRaises(expected_exception=ValueError):
            nouveau_thermostat = Ths.Thermostat.from_temperature(MAX_TEMPERATURE+4)

    def test_initialisation_temperature_trop_basse(self):
        with self.assertRaises(expected_exception=ValueError):
            nouveau_thermostat = Ths.Thermostat.from_temperature(MIN_TEMPERATURE-2)

    def test_initialisation_bonne_temperature(self):
        nouveau_thermostat = Ths.Thermostat.from_temperature(22)
        self.assertEqual(22, nouveau_thermostat.temperature)

# @unittest.skip
class test_modification_de_temperature(unittest.TestCase):

    def test_changer_temperature_trop_elevee(self):
       nouveau_thermostat = Ths.Thermostat()
       with self.assertRaises(expected_exception=ValueError):
           nouveau_thermostat.temperature = 40
       
    def test_changer_temperature_trop_basse(self):
       nouveau_thermostat = Ths.Thermostat()
       with self.assertRaises(expected_exception=ValueError):
           nouveau_thermostat.temperature = 2
       
    def test_changer_temperature_valide(self):
       nouveau_thermostat = Ths.Thermostat()
       with self.assertRaises(expected_exception=ValueError):
           nouveau_thermostat.temperature = 100
     
    def test_augmenter_1_degre_OK(self):
       nouveau_thermostat = Ths.Thermostat()
       nouveau_thermostat.temperature = 35
       with self.assertRaises(expected_exception=ValueError):
           nouveau_thermostat.augmenter_1_degre()
   
    def test_diminuer_1_degre_OK(self):
       nouveau_thermostat = Ths.Thermostat()
       nouveau_thermostat.temperature = 5
       with self.assertRaises(expected_exception=ValueError):
           nouveau_thermostat.diminuer_1_degre()


if __name__ == '__main__':
    unittest.main(verbosity=2)