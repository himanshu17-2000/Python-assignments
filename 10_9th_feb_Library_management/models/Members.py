from init_packages import db 
class Member(db.Model):
    __tablename__ = 'members'
    def __init__(self , name , email , phone):
        self.name = name 
        self.email = email 
        self.phone = phone 
    
    _id = db.Column(db.Integer ,primary_key = True) 
    name = db.Column(db.String(30) , nullable = False)
    email = db.Column(db.String(50) , nullable = False ,unique=True)
    phone = db.Column(db.String(10) , nullable = False ,unique=True)
