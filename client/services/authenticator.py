from model.user import User
from util.proxy import proxy
import jsonpickle

class Authenticator:
    def login(self, user: User):
        args = jsonpickle.encode({ "user": user }, unpicklable=False)
        
        data = proxy.do_operation("Authenticator", "login", args)

        print(data)
    
    def register(self, user: User):
        args = jsonpickle.encode({ "user": user }, unpicklable=False)

        data = proxy.do_operation("Authenticator", "register", args)
        
        print(data)