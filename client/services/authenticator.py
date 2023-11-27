from model.user import User
from util.proxy import proxy


class Authenticator:
    def login(self, user: User):
        proxy.do_operation("Authenticator", "login", {"user": user})

    def register(self, user: User):
        proxy.do_operation("Authenticator", "register", {"user": user})
