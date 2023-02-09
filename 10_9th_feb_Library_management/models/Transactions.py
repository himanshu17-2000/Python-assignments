from init_packages import db 
class Transaction(db.Model):
    __tablename__ = 'transactions'


    def __init__(self , book_id , member_id , book_name ,from_date):
        self.book_id = book_id
        self.member_id = member_id 
        self.book_name = book_name 
        self.from_date = from_date 
    
    tra_id = db.Column(db.Integer ,primary_key = True) 
    book_id = db.Column(db.Integer  , nullable = False ) 
    member_id =  db.Column(db.Integer  , nullable = False) 
    book_name = db.Column(db.String(50) , nullable = False)
    from_date = db.Column(db.DateTime , nullable = False)
    fine = db.Column(db.Integer  , default = 0 ) 

    
