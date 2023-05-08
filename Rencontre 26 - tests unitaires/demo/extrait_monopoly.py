class Terrain:
    pass
class Banque:
    pass

class Joueur:
    def __init__(self,montant_cash,list_terrains) -> None:
        pass

    def acheter(self,proprietaire,terrain:Terrain): 
        pass
            
kentucky = Terrain('Avenue Kentucky','rouge',True,220000)
pennsylvanie = Terrain('Avenue Pensylvanie','vert',True,320000)
promenade = Terrain('Promenade','bleu',True,400000)

banque = Banque(22000000,[kentucky,pennsylvanie,promenade])

joueur1 = Joueur(1000000,[])
joueur2 = Joueur(1000000,[])


print("joueur1 essaie d'acheter à la banque le terrain promenade")
joueur1.acheter(banque,promenade)

print('infos du joueur 1')
print(joueur1.montant_cash)
for terrain in joueur1.list_terrains:
    print(terrain)
#print(joueur1.list_terrains