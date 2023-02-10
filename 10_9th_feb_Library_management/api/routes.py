from flask import Blueprint ,request ,jsonify   
from models.Books import Book 
from models.Members import Member
from models.Transactions   import Transaction
from init_packages import db
from datetime import datetime , date

import requests


api = Blueprint('api' , __name__)
@api.route('/')
def home():
    # db.session.query(Book).delete()
    # url = "https://hapi-books.p.rapidapi.com/nominees/romance/2020"

    # headers = {
    #     "X-RapidAPI-Key": "9c254922afmsh6ac51f1b70c0bdep1978f1jsn7f9444b252cf",
    #     "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers)

    # books =  response.json()
    # for book in books :
    #      b = Book(book_name = book["book_name"] ,  book_author = book["author"] ,votes = book["votes"])
    #      db.session.add(b)
    
    # db.session.commit()

    return "<h1>Himanshu kumar Amb </h1>"

@api.route('/register' , methods =['POST'])
def register_member():
    name = request.json['name']
    email =request.json['email'] 
    phone = request.json['phone']

    
    m = Member(name  = name , email =email , phone = phone)
    
    if(Member.query.filter_by(email=email).one_or_none()  == None  or Member.query.filter_by(phone = phone).one_or_none()  == None):
            db.session.add(m)
            db.session.commit()
            return jsonify({"message" : "member added "}),200

    return jsonify({"message" : "member already access "}),401


@api.route('/borrow' , methods = ['POST'])
def borrow_book():
    boro_book_id = request.json['book_id']
    boro_member_id = request.json['member_id']
    boro_book_name = request.json['book_name']
    
    book = Book.query.filter_by(book_id = boro_book_id ).first()
    #=============== Making New Tuple in Transactions =============================
    if(book.book_stock <= 0 ):
         return jsonify({'message' : 'Book Out of stock'}) , 404
    t = Transaction.query.filter_by(book_id = boro_book_id , member_id = boro_member_id , borrowed = True ).first()
    print(t)
    if(t is not None and t.borrowed == True):
         return jsonify({'message' : 'First_return the previouly borrowed book'}) , 404
    
    Tra = Transaction(book_id = boro_book_id ,member_id = boro_member_id ,book_name = boro_book_name)
    db.session.add(Tra)

    # #============== Decrementing Count of Book by id  and  Inrementing Votes ======
    book.book_stock -= 1
    book.votes = book.votes + 1 
    #================ Commiting changes into the database ===========================
    db.session.commit()
    return jsonify({'message' : 'You have borrowed book for 14 days' , "tra_id":Tra.tra_id}) , 200


@api.route('/return' , methods = ['POST'])
def return_book():
    tra_id = request.json['tra_id']
    book_id = request.json['book_id']
    member_id = request.json['member_id']
    tra=Transaction.query.filter_by(book_id = book_id , member_id = member_id , tra_id= tra_id).first()
    # print(tra)
    book = Book.query.filter_by(book_id = tra.book_id).first()
    # print(book)
    book.book_stock +=1
    tra.borrowed = False

    f_date = tra.from_date
    # print(f_date , type(f_date))
    # t_date = date(2023, 2, 28)
    t_date = datetime.now().date()
    # print(f_date , type(t_date) )
    diff =(t_date - f_date)
    if(diff.days > 14):
        tra.fine = (diff.days-14)*100
    db.session.commit()
    # print("difrence between dates is :-" , str(diff.days) , type(diff.days) ) 
    return jsonify({'message' : 'Thanks for returning the book',
                    "fine":tra.fine}) , 200







@api.route('/transactions' , methods = ['GET'])
def transactions():
    # book = Book.query.filter_by(book_id = '1' ).first()
    # book.book_stock = 30
    # db.session.query(Transaction).delete()
    # db.session.commit()
    def get_dict(item):
          return {
               'tra_id':item.tra_id,
               'book_id':item.book_id,
               'member_id':item.member_id,
               'book_name':item.book_name,
               'from_date':str(item.from_date),
            #    'from_date':item.from_date,
               'fine' :item.fine ,
               'borrowed':item.borrowed 
                  }
    tras = Transaction.query.all()
    return jsonify(list(map(get_dict,tras))) 
    return ' 1 '
  
@api.route('/transactions/<int:_id>' , methods = ['GET'])
def transaction_by_id(_id):
   
    def get_dict(item):
          return {
               'tra_id':item.tra_id,
               'book_id':item.book_id,
               'member_id':item.member_id,
               'book_name':item.book_name,
               'from_date':str(item.from_date),
            #    'from_date':item.from_date,
               'fine' :item.fine ,
               'borrowed':item.borrowed 
                  }
    tras = Transaction.query.get(_id)
    t= [tras]
    return jsonify(list(map(get_dict,t))) 
  