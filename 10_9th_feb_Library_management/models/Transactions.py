from init_packages import db 
from datetime import datetime
class Transaction(db.Model):
    __tablename__ = 'transactions'
    tra_id = db.Column(db.Integer ,primary_key = True)
    book_id = db.Column(db.Integer  , nullable = False ) 
    member_id =  db.Column(db.Integer  , nullable = False) 
    book_name = db.Column(db.String(50) , nullable = False)
    from_date = db.Column(db.Date , nullable = False , default=datetime.now().date())
    borrowed = db.Column(db.Boolean , nullable = False , default = True)
    fine = db.Column(db.Integer  , default = 0 ) 
    

    def __init__(self , book_id , member_id , book_name):
        self.book_id = book_id
        self.member_id = member_id 
        self.book_name = book_name 

    def __str__(self):
        return str( "{"+str(self.tra_id) + " , " + str(self.book_id) + " , "+str(self.member_id) + " , " +str(self.book_name)+","+str(self.from_date) + " , "+str(self.borrowed) + " , "+str(self.fine)+" }" )
    
    



    
    


    
