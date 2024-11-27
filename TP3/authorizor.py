import authenticator
from exceptions import NotLoggedIn, NotPermitted, InvalidUsername


class Authorizor:
    """Gère les permissions pour les utilisateurs."""
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, permission_name):
        """Ajoute une nouvelle permission."""
        if permission_name in self.permissions:
            print(f"La permission '{permission_name}' existe déjà.")
        else:
            self.permissions[permission_name] = []

    def permit_user(self, permission_name, username):
        """Autorise un utilisateur à effectuer une action spécifique."""
        if permission_name not in self.permissions:
            raise KeyError(f"La permission '{permission_name}' n'existe pas.")
        if username not in self.authenticator.users:
            raise InvalidUsername(username)
        self.permissions[permission_name].append(username)

    def check_permission(self, permission_name, username):
        """Vérifie si un utilisateur a une permission."""
        if username not in self.authenticator.users:
            raise InvalidUsername(username)
        user = self.authenticator.users[username]
        if not user.logged_in:
            raise NotLoggedIn(username)
        if username not in self.permissions.get(permission_name, []):
            raise NotPermitted(username)
        print(f"L'utilisateur {username} a la permission '{permission_name}'.")

authorizor = Authorizor(authenticator)  # Instance globale