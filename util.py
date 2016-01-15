class UserAbstraction(object):
    def __init__(self, session):
        self.s = session
    
    def __getattr__(self, name):
        f = UserAbstraction.__dict__.get('_UserAbstraction__' + name)
        if f:
            return f(self) 
        raise AttributeError(
            "'UserAbstraction' object has no attribute '"+ name + "'")
    
    def __logged_in(self): # Temp, not how I wanna store it in the long run.
        user = self.s.get('logged_in')
        if user:
            return user == True
        return False
