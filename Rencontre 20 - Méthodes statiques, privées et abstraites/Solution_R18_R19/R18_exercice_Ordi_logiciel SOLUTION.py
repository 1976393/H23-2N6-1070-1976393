import csv


class Ordinateur:
    
    processeur = 'Ryzen 3600'
    memoire_vive = '16Go'
    
    def __init__(self,ID, adresseIP, processeur=None, memoire_vive=None) -> None:
        self.ID = ID
        self.adresseIP = adresseIP
        if (processeur != None):
            self.processeur = processeur
        if (memoire_vive != None):
            self.memoire_vive = memoire_vive
        pass
    
    def __str__(self) -> str:
        info = f' Ordinateur ID: {self.ID}, \n AdresseIP: {self.adresseIP}, \n Processeur: {self.processeur}, \n Mémoire vive: {self.memoire_vive}'
        return info
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur):
        cls.processeur = nouveau_processeur
        
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme):
        cls.memoire_vive = nouvelle_norme


          
class Poste_de_travail(Ordinateur):

    def __init__(self,ID, adresseIP, utilisation,processeur=None, memoire_vive=None) -> None:
        super().__init__(ID, adresseIP, processeur, memoire_vive)
        self.utilisation = utilisation
        self.liste_logiciels = []
        
    def installer_logiciel(self,logiciel, version):
        dict_logiciel = {'logiciel':logiciel, 'version': version} 
        if (dict_logiciel not in self.liste_logiciels):
            self.liste_logiciels.append(dict_logiciel)
        
    def desinstaller_logiciel(self,logiciel, version):
        dict_logiciel = {'logiciel':logiciel, 'version': version}
        self.liste_logiciels.pop(dict_logiciel)
        
    def imprimer_liste_logiciels(self):
        for logiciel in self.liste_logiciels:
            print(f'\t {logiciel}')
    
   
ordi_prof = Poste_de_travail('LPFINFOPORT001', '192.168.221.21', '*', memoire_vive='32Go')
ordi_reseau = Poste_de_travail('LLBINFO060208', '192.168.219.21', 'info-réseau')
ordi_prog = Poste_de_travail('LLBINFO060505', '192.168.220.17', 'info-prog')

def charger_logiciels(poste):
    with open('logiciels2022_2023.csv ','r',encoding='utf8') as data_CSV:
        csv_data = csv.reader(data_CSV,delimiter=';')
        #sauter la première ligne #
        next(csv_data)
        for line in csv_data:
            if (poste.utilisation == line[2] or poste.utilisation == '*' or line[2]=='info'):
                poste.installer_logiciel(line[0],line[1])
             
             
charger_logiciels(ordi_prof)
print(f"Logiciels du prof30 ({len(ordi_prof.liste_logiciels)}):")
ordi_prof.imprimer_liste_logiciels()
charger_logiciels(ordi_reseau)
print(f"Logiciels de réseau ({len(ordi_reseau.liste_logiciels)}):")
ordi_reseau.imprimer_liste_logiciels()
charger_logiciels(ordi_prog)
print(f"Logiciels de prog ({len(ordi_prog.liste_logiciels)}):")
ordi_prog.imprimer_liste_logiciels()
print(f'Mémoire vive des ordinateurs:')
print(f'Poste de prof: {ordi_prof.memoire_vive}')
print(f'Poste de réseau: {ordi_reseau.memoire_vive}')
print(f'Poste de prog: {ordi_prog.memoire_vive}')
print('On va maintenant upgrader la mémoire vive de tous les ordis à 32Go')
Ordinateur.upgrader_memoire('32Go')
print(f'Mémoire vive des ordinateurs, après l\'upgrade:')
print(f'Poste de prof: {ordi_prof.memoire_vive}')
print(f'Poste de réseau: {ordi_reseau.memoire_vive}')
print(f'Poste de prog: {ordi_prog.memoire_vive}')
