from datetime import datetime, timedelta

class Emprunt:
    def __init__(self, livre, personne, jours_emprunt=14):
        self.livre = livre
        self.personne = personne
        self.date_emprunt = datetime.now()
        self.date_retour = self.date_emprunt + timedelta(days=jours_emprunt)
        livre.disponible = False

    def afficher_details(self):
        print(f"Livre emprunté : {self.livre.titre}")
        print(f"Par : {self.personne.prenom} {self.personne.nom}")
        print(f"Date d'emprunt : {self.date_emprunt.strftime('%Y-%m-%d')}")
        print(f"Date de retour prévue : {self.date_retour.strftime('%Y-%m-%d')}")