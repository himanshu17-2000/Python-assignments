from extenstions import db

class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), unique=True , nullable = False) 
    password = db.Column(db.String(50), nullable = False)
    admin   = db.Column(db.Boolean )
    
    # admin = db.Column(db.Bool, nullable = False)
    def __init__(self,username,password,admin):
        self.username = username 
        self.password = password 
        self.admin = admin 
    def __str__(self) -> str:
        return str(self.id)+" "+str(self.username)+" "+str(self.password)+" "+str(self.admin)+" ."
