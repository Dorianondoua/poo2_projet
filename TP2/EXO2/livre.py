class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def afficher_details(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        print(f"Livre: {self.titre}, Auteur: {self.auteur}, Année: {self.annee}, Statut: {statut}")