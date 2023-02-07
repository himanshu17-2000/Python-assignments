from app import db
class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), unique=True , nullable = False) 
    password = db.Column(db.String(50), nullable = False)
    def __init__(self,username,password):
        self.username = username 
        self.password = password 
