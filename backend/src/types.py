import flask_login

class User(flask_login.UserMixin):
    def __init__(self, id, password, email, admin=False, **kwargs):
        self.id = id
        self.password = password
        self.email = email
        self.admin = False
    def __dict__(self):
        d = {k: v for k, v in vars(self) if k in
             ["id","password","email","admin"]}
        return d
    def __repr__(self):
        return f'{self.id} (self.email)'
