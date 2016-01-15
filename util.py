class BaseAbstraction(object):
    def __getattr__(self, name):
        c = self.__class__
        f = c.__dict__.get(
            '_' + c.__name__ + '__' + name)
        if f:
            return f(self) 
        raise AttributeError(
            "'" + c.__name__ + "' object has no attribute '" + name + "'")

class UserAbstraction(BaseAbstraction):
    def __init__(self, session):
        self.s = session
    
    def __logged_in(self): # Temp, not how I wanna store it in the long run.
        user = self.s.get('logged_in')
        if user:
            return user == True
        return False
