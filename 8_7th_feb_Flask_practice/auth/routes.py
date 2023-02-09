from flask import request , jsonify ,Blueprint
from flask_jwt_extended import create_access_token
from extenstions import db 
from models.user import User
auth = Blueprint('auth' , __name__ )
@auth.route('/register' ,methods =['POST'])
def register():
    username = request.json['username'] 
    password =request.json['password'] 
    admin =request.json['admin'] 
    print(admin)
    user = User.query.filter_by(username = username ).one_or_none() 
    if(user is not None):
        return jsonify({"message" :"username already exists "}),400
    
    user = User(username=username , password=password , admin=admin) 
    print(user.admin)
    db.session.add(user) 
    db.session.commit()
    return jsonify(message = 'user created') 

@auth.route('/login' , methods =['POST'])
def login():
    username = request.json['username'] 
    password =request.json['password'] 
    user = User.query.filter_by(username = username , password= password).one_or_none() 
    if(user is not None ):
        access_token = create_access_token(identity = user.id)
        response = jsonify({"message" :"success" ,"access_token" : access_token })
        return response,200
    else:
        return jsonify({"message" :"invalid credentials" }) , 401
    


@auth.route('/getusers' , methods = ["GET"])
def Get_Users():
    all_users = User.query.all() 
    def get_dict(item):
        return {"username" :item.username , "password" :item.password , "id" :item.id ,"admin" :item.admin}

    return jsonify(list(map(get_dict , all_users))),200

@auth.route('/delete/<int:_id>' , methods = ["DELETE"])
def Delete_users(_id):
    pro = User.query.get(_id)
    db.session.delete(pro)
    db.session.commit() 
    return f"detleted {_id}" , 200