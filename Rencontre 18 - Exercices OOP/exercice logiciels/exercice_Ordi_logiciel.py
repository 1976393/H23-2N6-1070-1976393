import csv
import os
os.chdir(os.path.dirname(__file__))

class Ordinateur:
    processeur_d = "Ryzen 3600"
    memoire_vive_d = "16Go"
    
    def __init__(self,ID, adresseIP, processeur=processeur_d, memoire_vive=memoire_vive_d) -> None:
        self.id = ID
        self.adressIP = adresseIP
        self.processeur = processeur
        self.memoire_vive = memoire_vive
        
    def __str__(self) -> str:
        pass
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        cls.processeur_d = nouveau_processeur
        
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        cls.memoire_vive_d = nouvelle_norme
    
   
class Poste_de_travail(Ordinateur):
    
    def __init__(self,ID, adresseIP, utilisation,processeur, memoire_vive) -> None:
        super().__init__(ID,adresseIP,processeur,memoire_vive)
        self.utilisation = utilisation
        
    
    def installer_logiciel(self) -> None:
        liste_logiciel = []
        with open("logiciels2022_2023.csv","r",encoding="utf-8") as file:
            csv_reader = csv.reader(file,delimiter=";")
            next(csv_reader)
            for line in csv_reader:
                if self.utilisation == "*":
                    log_ver ={"logiciel" : "", "version" : ""}
                    log_ver.update({"logiciel" : line[0],"version" : line[1]})
                    liste_logiciel.append(log_ver)
                elif self.utilisation == "info-réseau":
                    if line[2] == "info-réseau" or line[2] == "info":
                        log_ver ={"logiciel" : "", "version" : ""}
                        log_ver.update({"logiciel" : line[0],"version" : line[1]})
                        liste_logiciel.append(log_ver)
                elif self.utilisation == "info-prog":
                    if line[2] == "info-prog" or line[2] == "info":
                        log_ver ={"logiciel" : "", "version" : ""}
                        log_ver.update({"logiciel" : line[0],"version" : line[1]})
                        liste_logiciel.append(log_ver)
            return liste_logiciel
            
    def desinstaller_logiciel(self,logiciel,version) -> None:
        pass 
    
    def imprimer_liste_logiciels(self) -> None:
        for line in self.installer_logiciel():
            print(line,end="\n")
        
    
    
ordinateur_prof = Poste_de_travail("LPFINFOPORT001","192.168.221.21","*","Ryzen 3600","32Go")
ordinateur_reseau = Poste_de_travail("LLBINFO60208","192.168.219.21","info-réseau","Ryzen 3600","16Go")
ordinateur_prog = Poste_de_travail("LLBINFO060505","192.168.220.17","info-prog","Ryzen 3600","16Go")

print(f'Logiciel pour prof({len(ordinateur_prof.installer_logiciel())})')
ordinateur_prof.imprimer_liste_logiciels()
print(80*"_")
print(f'Logiciel pour réseau({len(ordinateur_reseau.installer_logiciel())})')
ordinateur_reseau.imprimer_liste_logiciels()
print(80*"_")
print(f'Logiciel pour prog({len(ordinateur_prog.installer_logiciel())})')
ordinateur_prog.imprimer_liste_logiciels()

