
from livre import Livre
from personne import Personne
from bibliothèque import Bibliotheque

# Initialiser la bibliothèque
biblio = Bibliotheque()

# Création d'un membre par défaut
personne1 = Personne("Doe", "John", 101)

# Fonction principale pour afficher le menu
def afficher_menu():
    print("\n=== MENU BIBLIOTHÈQUE ===")
    print("1. Ajouter un livre")
    print("2. Afficher les livres disponibles")
    print("3. Afficher les livres empruntés")
    print("4. Emprunter un livre")
    print("5. Retourner un livre")
    print("6. Quitter")
    choix = input("Entrez votre choix : ")
    return choix

# Fonction pour gérer les interactions utilisateur
def main():
    while True:
        choix = afficher_menu()
        if choix == "1":
            titre = input("Entrez le titre du livre : ")
            auteur = input("Entrez l'auteur du livre : ")
            annee = input("Entrez l'année de publication : ")
            livre = Livre(titre, auteur, annee)
            biblio.ajouter_livre(livre)

        elif choix == "2":
            biblio.afficher_livres_disponibles()

        elif choix == "3":
            biblio.afficher_livres_empruntes()

        elif choix == "4":
            titre = input("Entrez le titre du livre à emprunter : ")
            livre = next((l for l in biblio.livres if l.titre == titre and l.disponible), None)
            if livre:
                biblio.emprunter_livre(livre, personne1)
            else:
                print(f"Le livre '{titre}' n'est pas disponible ou n'existe pas.")

        elif choix == "5":
            titre = input("Entrez le titre du livre à retourner : ")
            livre = next((l for l in biblio.livres if l.titre == titre and not l.disponible), None)
            if livre:
                biblio.retourner_livre(livre)
            else:
                print(f"Le livre '{titre}' n'a pas été emprunté.")

        elif choix == "6":
            print("Merci d'avoir utilisé le système de gestion de la bibliothèque.")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()