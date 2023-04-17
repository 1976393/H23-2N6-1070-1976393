#Voyez l'énoncé R20 Exercice 2 Calculer_paie.docx

#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    def __init__(self) -> None:
        self.liste_employes = []
        
    def calculer_paie(self):
        for i in self.liste_employes:
            print(f'Paie de {i.id_employee} - {i.nom} \n -montant net de : {i.calculer_paie()} \n')
            
            
class Employe(ABC):
    def __init__(self,id_employee,nom) -> None:
        self.id_employee = id_employee
        self.nom = nom
    
    @abstractmethod
    def calculer_paie():
        pass
    
class Employe_salarie(Employe):
    def __init__(self, id_employee, nom,salaire_par_semaine) -> None:
        super().__init__(id_employee, nom)
        self.salaire_par_semaine = salaire_par_semaine
    def calculer_paie(self):
        return self.salaire_par_semaine
 
class Employe_heure(Employe):  
    def __init__(self, id_employee, nom,heures_travaillees,taux_horaire) -> None:
        super().__init__(id_employee, nom)
        self.heures_travaillees = heures_travaillees
        self.taux_horaire = taux_horaire
    def calculer_paie(self):
        return (self.heures_travaillees * self.taux_horaire)
    
class Employe_Commission(Employe_salarie):  
    def __init__(self,id_employee,nom,salaire_par_semaine,commission) -> None:
        super().__init__(id_employee,nom,salaire_par_semaine)
        self.commission = commission
    def calculer_paie(self):
        return (self.salaire_par_semaine + self.commission)
        
    
 

#instanciation des objets 
emp1 = Employe_salarie(1,"Marc Tremblay",2100)
emp2 = Employe_heure(2,"Pierre Johnson",40,22)
emp3 = Employe_Commission(3,"Luc Toupin",1400,600)

sys_paie = Systeme_de_paie()
sys_paie.liste_employes.append(emp1)
sys_paie.liste_employes.append(emp2)
sys_paie.liste_employes.append(emp3)
sys_paie.calculer_paie()