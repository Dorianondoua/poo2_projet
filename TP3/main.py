
from authenticator import authenticator
from authorizor import authorizor
from exceptions import AuthException

def afficher_menu():
    print("\n=== MENU ===")
    print("1. Ajouter un utilisateur")
    print("2. Connexion")
    print("3. Déconnexion")
    print("4. Ajouter une permission")
    print("5. Autoriser un utilisateur")
    print("6. Vérifier une permission")
    print("7. Quitter")
    choix = input("Entrez votre choix : ")
    return choix

def main():
    while True:
        choix = afficher_menu()
        try:
            if choix == "1":
                username = input("Entrez le nom d'utilisateur : ")
                password = input("Entrez le mot de passe : ")
                authenticator.add_user(username, password)
                print(f"Utilisateur '{username}' ajouté.")

            elif choix == "2":
                username = input("Entrez le nom d'utilisateur : ")
                password = input("Entrez le mot de passe : ")
                authenticator.login(username, password)

            elif choix == "3":
                username = input("Entrez le nom d'utilisateur : ")
                authenticator.logout(username)

            elif choix == "4":
                permission = input("Entrez le nom de la permission : ")
                authorizor.add_permission(permission)
                print(f"Permission '{permission}' ajoutée.")

            elif choix == "5":
                permission = input("Entrez le nom de la permission : ")
                username = input("Entrez le nom d'utilisateur : ")
                authorizor.permit_user(permission, username)
                print(f"L'utilisateur '{username}' a reçu la permission '{permission}'.")

            elif choix == "6":
                permission = input("Entrez le nom de la permission : ")
                username = input("Entrez le nom d'utilisateur : ")
                authorizor.check_permission(permission, username)

            elif choix == "7":
                print("Au revoir !")
                break

            else:
                print("Choix invalide.")

        except AuthException as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()