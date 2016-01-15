import database

class APIManager(object):
    def __init__(self, session, request):
        self.s = session
        self.r = request
    
    def logged_in(self):
        user = self.s.get('user')
        if user:
            return user.get('logged_in') == True
        return False
    
    def log_in(self):
        user = database.check_user(username, password)
        if user == None:
            return None
        elif user == False:
            return False
        else:
            return True

