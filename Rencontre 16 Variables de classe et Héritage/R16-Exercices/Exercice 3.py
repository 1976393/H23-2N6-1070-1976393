from numbers import Real


class Personne:
    def __init__(self,nom,prenom,date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        
class Employe(Personne):
    def __init__(self, nom, prenom, date_naissance,NAS,poste,salaire) -> None:
        super().__init__(nom, prenom, date_naissance)
        self.NAS = NAS
        self.poste = poste
        self.salaire = salaire
        
class Realisateur(Employe):
    def __init__(self, nom, prenom, date_naissance, NAS, poste, salaire,bonus) -> None:
        super().__init__(nom, prenom, date_naissance, NAS, poste, salaire)
        self.bonus = bonus
        
class Acteur(Employe):
    def __init__(self, nom, prenom, date_naissance, NAS, poste, salaire,role) -> None:
        super().__init__(nom, prenom, date_naissance, NAS, poste, salaire)
        self.role = role
        
class Film:
    def __init__(self,nom, date_sortie,liste_employes=[]) -> None:
        self.nom = nom
        self.liste_employes = liste_employes
        self.date_sortie = date_sortie
    
film1 = Film("Titanic","19 décembre 1997",[])
film2 = Film("Abyss","9 aout 1989",[])
film3 = Film("Avatar","18 décembre 2009",[])
réalisateur = Realisateur("Cameroun","James","16 aout 1954","","","","2")
employe1_0 = Employe("bob","bob","2 aout 2222","","filmeur","")
employe1_1 = Employe("bobby","bobby","3 aout 3333","","stunt_actor","")
employe1_2 = Acteur("bobber","bobber","3 septembre 3333","","acteur","","acteur_principal")

employe2_0 = Employe("tam","tam","4 aout 4424","","filmeur","")
employe2_1 = Employe("tammy","tammy","4 aout 3434","","stunt_actor","")
employe2_2 = Acteur("tammer","tammer","5 aout 3222","","acteur","","acteur_principal")

employe3_0 = Employe("Emmy","Emmy","1 aout 1213","","filmeuse","")
employe3_1 = Employe("Emile","Emile","4 aout 2223","","stunt_actor","")
employe3_2 = Acteur("Emily","Emily","9 aout 8921","","acteuse","","acteuse_principale")

film1.liste_employes.append(employe1_0)
film1.liste_employes.append(employe1_1)
film1.liste_employes.append(employe1_2)

film2.liste_employes.append(employe2_0)
film2.liste_employes.append(employe2_1)
film2.liste_employes.append(employe2_2)

film3.liste_employes.append(employe3_0)
film3.liste_employes.append(employe3_1)
film3.liste_employes.append(employe3_2)

print(réalisateur.__dict__)
print(film1.__dict__)