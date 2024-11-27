class Personne:
    def __init__(self, nom, prenom, num_membre):  # Correction ici
        self.nom = nom
        self.prenom = prenom
        self.num_membre = num_membre

    def afficher_details(self):
        print(f"Personne: {self.prenom} {self.nom}, Numéro Membre: {self.num_membre}")