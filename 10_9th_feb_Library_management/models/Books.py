from init_packages import db 
class Book(db.Model):
    __tablename__ = 'books'
    
    def __init__(self, book_name , book_author , votes):
        self.book_name = book_name 
        self.book_author = book_author 
        self.votes = votes
    
    def __str__(self):
        return "{ "+ str(self.book_id)+" , "+ str(self.book_name) + " , "+str(self.book_author) + " , " +str(self.votes)+" , "+ str(self.book_stock)  + " }" 
    
    book_id = db.Column(db.Integer ,primary_key = True) 
    book_name = db.Column(db.String(50) , nullable = False)
    book_author = db.Column(db.String(50) , nullable = False)

    book_stock =db.Column(db.Integer ,nullable = False , default = 30  )

    votes = db.Column(db.Integer , default = 0)



    
