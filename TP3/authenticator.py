
from utilisateur import Utilisateur
from exceptions import UsernameAlreadyExists, InvalidUsername, InvalidPassword

class Authenticator:
    """Gère les utilisateurs et leur connexion."""
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        """Ajoute un nouvel utilisateur."""
        if username in self.users:
            raise UsernameAlreadyExists(username)
        self.users[username] = Utilisateur(username, password)

    def login(self, username, password):
        """Connecte un utilisateur."""
        if username not in self.users:
            raise InvalidUsername(username)
        user = self.users[username]
        if not user.check_password(password):
            raise InvalidPassword(username)
        user.logged_in = True
        print(f"L'utilisateur {username} est connecté.")

    def logout(self, username):
        """Déconnecte un utilisateur."""
        if username not in self.users:
            raise InvalidUsername(username)
        self.users[username].logged_in = False
        print(f"L'utilisateur {username} est déconnecté.")

authenticator = Authenticator()  # Instance globale