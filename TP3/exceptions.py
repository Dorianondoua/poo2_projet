
class AuthException(Exception):
    """Classe de base pour les exceptions d'authentification."""
    def _init_(self, username, user=None):
        super().__init__(username)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    """Exception levée lorsque le nom d'utilisateur existe déjà."""
    pass


class InvalidUsername(AuthException):
    """Exception levée lorsque le nom d'utilisateur est invalide."""
    pass


class InvalidPassword(AuthException):
    """Exception levée lorsque le mot de passe est incorrect."""
    pass


class NotLoggedIn(AuthException):
    """Exception levée lorsqu'un utilisateur tente d'effectuer une action sans être connecté."""
    pass


class NotPermitted(AuthException):
    """Exception levée lorsqu'un utilisateur n'a pas les permissions requises."""
    pass