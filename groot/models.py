from groot import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False, unique=False)
    last_name = db.Column(db.String(30), nullable=False, unique=False)
    nick_name = db.Column(db.String(30), nullable=False, unique=False)
    hash_pw = db.Column(db.String(200), nullable=False, unique=False)

    def __init__(self,email,first_name,last_name,nick_name,hash_pw):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.hash_pw = hash_pw


    def __repr__(self):
        return {'email':self.email, 'first_name':self.first_name,'last_name':self.last_name, 'nick_name':self.nick_name,'hash_pw':self.hash_pw}
      
      #  return '<User: {}>'.format(self.username)