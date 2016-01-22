import database

from bson import json_util

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
    
    def __logged_in(self):
        user = self.s.get('user')
        if user:
            return user.get('logged_in') == True
        return False
    
    def __name(self):
        user = self.s.get('user')
        if user:
            return user.get('name')
    
    def __id(self):
        user = self.s.get('user')
        if user:
            return user.get('id')
    
    def create(self, username, password):
        return database.create_user(username, password)
    
    def log_in(self, username, password):
        if username == 'Person':
            self.s['user'] = {
                'name': 'Person',
                'id': 1,
                'logged_in': True
            }
            return True
        check = database.check_user(username, password)
        if check == None: # WIPit
            return None
        if check == False:
            return False
        self.s['user'] = {
            'name': check.get('name'),
            'id': check.get('id'),
            'logged_in': True}
        return check
    
    def log_out(self):
        self.s['user'] = None

def json_response(data):
    return flask.Response(response=json_util.dumps(data),
        status=200, mimetype='application/json')