class Terrain:
    def __init__(self,nom,couleur,prix) -> None:
        self.nom = nom
        self.couleur = couleur
        self.prix = prix
        
    def __str__(self) -> str:
       pass
   
class Banque:
    def __init__(self,montant_cash,liste_terrains) -> None:
        self.montant_cash = montant_cash
        self.liste_terrains = liste_terrains
        

class Joueur:
    def __init__(self,montant_cash,liste_terrains) -> None:
        self.montant_cash = montant_cash
        self.liste_terrains = liste_terrains
        
    def acheter(self,proprietaire:Banque,terrain:Terrain): # indique que les variables passée doit êtres de types spécifiques 
        if s
    
terrain_1 = Terrain("Avenue Kentucky","rouge",220000)
terrain_2 = Terrain("Avenue Pennsylvanie","bleu",320000)
terrain_3 = Terrain("Promenade","bleu",400000)

banque = Banque(22000000,["Avenue Kentucky","Avenue Pennsylvanie","Promenade"])

joueur_1 = Joueur(1000000,[])
joueur_2 = Joueur(1000000,[])
