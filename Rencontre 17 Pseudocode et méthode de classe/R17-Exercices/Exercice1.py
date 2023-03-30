from ast import With
import csv

class Achat:
    def __init__(self,id,budget,liste_equipment,liste_equipment_a_acheter,est_payer) -> None:
        self.id = id
        self.budget = budget
        self.liste_equipment = liste_equipment
        self.liste_equipment_a_acheter = liste_equipment_a_acheter
        self.est_payer = est_payer
        
    def payer(self):
        self.budget 
        pass
        
class equipment():
    def __init__(self, id,nom_equiment,cle,model,qty,prix_unitaire) -> None:
        self.id = id
        self.nom_equipment = nom_equiment
        self.cle = cle
        self.model = model
        self.qty = qty
        self.prix_unitaire = prix_unitaire
        
    def from_string():
        pass
    
    @classmethod
    def from_list(cls,emp_string):
        
        pass

achat_1 = Achat(420,20000,[],[],"")

with open("AchatsDepartement2023.csv","r",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = ";")
        next(csv_reader)
        liste = []
        liste_a_acheter =[]
        for line in csv_reader:
            liste.append(line)
        achat_1.liste_equipment = liste
       
            
            
    

    
            
        
    # print(liste)