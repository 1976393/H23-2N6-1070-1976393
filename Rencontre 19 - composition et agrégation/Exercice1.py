from csv import list_dialects
from pyparsing import NoMatch
from datetime import datetime

class Employe:
    def __init__(self,id,nom,prenom,role,salaire) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.role = role
        self.salaire = salaire

    def __str__(self):
        return(f'{self.nom}')

class Programmer(Employe):
    def __init__(self, id, nom, prenom, role, salaire,liste_fonctions = []) -> None:
        super().__init__(id, nom, prenom, role, salaire)
        self.liste_fonctions = liste_fonctions
        
    def coder(self,fonction):
        self.liste_fonctions.append(fonction)
            

class Designer(Employe):
    def __init__(self, id, nom, prenom, role, salaire,liste_artifacts = []) -> None:
        super().__init__(id, nom, prenom, role, salaire)
        self.liste_artifacts = liste_artifacts
        
    def dessiner(self,artifact):
        self.liste_artifacts.append(artifact)
            
        
class Tech_Reseau(Employe):
    def __init__(self, id, nom, prenom, role, salaire,liste_interventions = []) -> None:
        super().__init__(id, nom, prenom, role, salaire)
        self.liste_interventions = liste_interventions
        
    def intervenir(self,intervention):
            self.liste_interventions.append(intervention)
        
class Equipe:
    def __init__(self,nom,liste_employes = []) -> None:
        self.nom = nom
        self.liste_employes = liste_employes
        
    def __str__(self):
        return self.nom
        
    def ajouter_employe(self,employe):
        dict_employe = {"nom" : employe,"date_début": datetime.date.today(),"date_fin" : None}
        self.liste_employes.append(dict_employe)
    
    def enlever_employe(self,employe):
        for dict in self.liste_employes:
            if dict["nom"] == employe:
                dict["date_fin"] = datetime.date.today()
    def imprimer_employe(self):
        cpt = 0
        for dict in self.liste_employes:
            if dict["date_fin"] == None:
                cpt += 1
        print(f'Nom de l\'équpie {self}, nombre d\'employés = {cpt}')
        for i in self.liste_employes:
            print(__dict__(i))
        
class Logiciel:
    def __init__(self,nom,etat,liste_equipes = []) -> None:
        self.nom = nom
        self.etat = etat
        self.liste_equipes = liste_equipes
        
    def ajouter_equipe(self,equipe):
        self.liste_equipes.append(equipe)

log1 = Logiciel("ZenithSuit","Developpement",)
equ1 = Equipe("Developpement",)
log1.ajouter_equipe(equ1)
print(log1.liste_equipes)