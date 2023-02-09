from flask import Blueprint ,request ,jsonify   
from models.Books import Book 
from models.Members import Member
from models.Transactions   import Transaction
from init_packages import db
from datetime import datetime
from datetime import date

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
def borrow():
    boro_book_id = request.json['book_id']
    boro_member_id = request.json['member_id']
    boro_book_name = request.json['book_name']
    boro_from_date = date.today()
    Tra = Transaction(book_id = boro_book_id ,member_id = boro_member_id ,book_name =boro_book_name ,from_date =boro_from_date   ) 
    
  
  