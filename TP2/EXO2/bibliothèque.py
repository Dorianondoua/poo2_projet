
from emprunt import Emprunt

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.emprunts = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre.titre}")

    def afficher_livres_disponibles(self):
        print("\nLivres disponibles :")
        for livre in self.livres:
            if livre.disponible:
                livre.afficher_details()

    def afficher_livres_empruntes(self):
        print("\nLivres empruntés :")
        for emprunt in self.emprunts:
            emprunt.afficher_details()

    def emprunter_livre(self, livre, personne):
        if livre.disponible:
            emprunt = Emprunt(livre, personne)
            self.emprunts.append(emprunt)
            print(f"{personne.prenom} {personne.nom} a emprunté le livre : {livre.titre}")
        else:
            print(f"Le livre '{livre.titre}' est déjà emprunté.")

    def retourner_livre(self, livre):
        for emprunt in self.emprunts:
            if emprunt.livre == livre:
                livre.disponible = True
                self.emprunts.remove(emprunt)
                print(f"Le livre '{livre.titre}' a été retourné.")
                return
        print(f"Le livre '{livre.titre}' n'était pas emprunté.")