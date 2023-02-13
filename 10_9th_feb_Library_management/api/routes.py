from flask import Blueprint, request, jsonify
from models.Books import Book
from models.Members import Member
from models.Transactions import Transaction
from init_packages import db
from datetime import datetime, date

import requests

api = Blueprint("api", __name__)


@api.route("/")
def home():
    
    url = "https://hapi-books.p.rapidapi.com/nominees/romance/2020"

    headers = {
        "X-RapidAPI-Key": "9c254922afmsh6ac51f1b70c0bdep1978f1jsn7f9444b252cf",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    books =  response.json()
    # print(books)

    for book in books :
         b = Book(book_name = book["name"] ,  book_author = book["author"] ,votes = book["votes"])
         db.session.add(b)

    db.session.commit()

    return "<h1>Himanshu kumar amb </h1>" , 200

@api.route("/register", methods=["POST"])
def register_member():
    name = request.json["name"]
    email = request.json["email"]
    phone = request.json["phone"]
    m = Member(name=name, email=email, phone=phone)  # naming coonvention
    if (
        Member.query.filter_by(email=email).one_or_none() == None
        or Member.query.filter_by(phone=phone).one_or_none() == None
    ):
        db.session.add(m)
        db.session.commit()
        return jsonify({"message": "member added "}), 200

    return jsonify({"message": "member already access "}), 401


@api.route("/getmembers", methods=["GET"])
def get_members():
    user = Member.query.all()

    def get_dict(item):
        return {
            "member_id": item._id,
            "name": item.name,
            "email": item.email,
            "phone": item.phone,
        }

    arr = list(map(get_dict, user))

    return jsonify(arr), 200


@api.route("/delmember/<int:_id>", methods=["GET"])
def delete_member(_id):
    user = Member.query.get(_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Member Deleted"}), 200


@api.route("/borrow", methods=["POST"])
def borrow_book(): 
    boro_book_id = request.json["book_id"]
    boro_member_id = request.json["member_id"]
    # ================= checking if user id exists ================================
    user = Member.query.filter_by(_id=boro_member_id)
    if user is None:
        return jsonify({"message": "Member Does not exists , Please register"})

    # =============== Making New Tuple in Transactions =============================
    book = Book.query.filter_by(book_id=boro_book_id).first()
    if book.book_stock <= 0:
        return jsonify({"message": "Book Out of stock"}), 404

    t = Transaction.query.filter_by(
        book_id=boro_book_id, member_id=boro_member_id, borrowed=True
    ).first()
    print(t)
    if t is not None and t.borrowed == True:
        return jsonify({"message": "First_return the previouly borrowed book"})

    Tra = Transaction(
        book_id=boro_book_id, member_id=boro_member_id, book_name=book.book_name
    )
    db.session.add(Tra)

    # #============== Decrementing Count of Book by id  and  Inrementing Votes ======
    book.book_stock -= 1
    book.votes = book.votes + 1
    # ================ Commiting changes into the database ===========================
    db.session.commit()
    return jsonify({"message": "Thanks for Borrowing Book", "tra_id": Tra.tra_id}), 200


@api.route("/return", methods=["POST"])
def return_book():
    tra_id = request.json["tra_id"]
    # book_id = request.json['book_id']
    # member_id = request.json['member_id']
    test = Transaction.query.filter_by(tra_id=tra_id, borrowed=False).first()
    if test is not None:
        return (
            jsonify(
                {"message": "Old Record , Book already Returned", "rent": test.fine}
            ),
            200,
        )

    tra = Transaction.query.filter_by(tra_id=tra_id, borrowed=True).first()

    # print(tra)
    book = Book.query.filter_by(book_id=tra.book_id).first()

    # print(book)
    book.book_stock += 1
    tra.borrowed = False

    f_date = tra.from_date
    # print(f_date , type(f_date))
    # t_date = date(2023, 2, 28)
    t_date = datetime.now().date()
    # print(f_date , type(t_date) )
    diff = t_date - f_date
    if diff.days > 14:
        tra.fine = (diff.days) * 10
    db.session.commit()
    # print("difrence between dates is :-" , str(diff.days) , type(diff.days) )
    return jsonify({"message": "Book has been Returned", "rent": tra.fine}), 200


# ======================================================== reports utiliy ==============================================
@api.route("/popular", methods=["GET"])
def popular():
    def get_dict(item):
        return {
            "book_id": item.book_id,
            "book_name": item.book_name,
            "book_author": item.book_author,
            "book_stock": item.book_stock,
            "votes": item.votes,
        }

    data = Book.query.all()

    arr = sorted(list(map(get_dict, data)), key=lambda x: x["votes"])

    return jsonify(arr[::-1]), 200


# ======================================================== data utility routes just to see data ==========================


@api.route("/books", methods=["GET"])
def fetchbooks():
    def get_dict(item):
        return {
            "book_id": item.book_id,
            "book_name": item.book_name,
            "book_author": item.book_author,
            "book_stock": item.book_stock,
            "votes": item.votes,
        }

    data = Book.query.all()

    return jsonify(list(map(get_dict, data))), 200


@api.route("/addbook", methods=["POST"])
def addbook():
    name = request.json["book_name"]
    author = request.json["book_author"]
    stock = request.json["book_stock"]
    prevbook = Book.query.filter_by(
        book_name=name, book_author=author).one_or_none()
    if prevbook is not None:
        prevbook.book_stock += stock
    else:
        db.session.add(prevbook)
    db.session.commit()
    return jsonify({"message": "Book Added"}), 200


@api.route("/deletebook/<int:_id>", methods=["POST"])
def deletebook(_id):
    book = Book.query.filter_by(book_id=_id)
    if book is not None:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book Deleted"}), 200

    return jsonify({"message": "Book Not exists"}), 404


@api.route("/transactions", methods=["GET"])
def transactions():
    # book = Book.query.filter_by(book_id ="1" ).first()
    # book.book_stock = 30
    # db.session.query(Transaction).delete()
    # db.session.commit()
    def get_dict(item):
        return {
            "tra_id": item.tra_id,
            "book_id": item.book_id,
            "member_id": item.member_id,
            "book_name": item.book_name,
            "from_date": str(item.from_date),
            #    'from_date':item.from_date,
            "fine": item.fine,
            "borrowed": item.borrowed,
        }

    tras = Transaction.query.all()
    return jsonify(list(map(get_dict, tras)))
    return " 1 "


@api.route("/transactions/<int:_id>", methods=["GET"])
def transaction_by_id(_id):
    def get_dict(item):
        return {
            "tra_id": item.tra_id,
            "book_id": item.book_id,
            "member_id": item.member_id,
            "book_name": item.book_name,
            "from_date": str(item.from_date),
            #    'from_date':item.from_date,
            "fine": item.fine,
            "borrowed": item.borrowed,
        }

    tras = Transaction.query.get(_id)
    t = [tras]
    return jsonify(list(map(get_dict, t)))
