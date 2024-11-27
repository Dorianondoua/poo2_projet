
import hashlib

class Utilisateur:
    """Représente un utilisateur avec un nom et un mot de passe crypté."""
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._encrypt_password(password)
        self.logged_in = False

    def _encrypt_password(self, password):
        """Crypte le mot de passe à l'aide de SHA-256."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password):
        """Vérifie si le mot de passe fourni correspond au mot de passe crypté."""
        return self.password_hash == self._encrypt_password(password)