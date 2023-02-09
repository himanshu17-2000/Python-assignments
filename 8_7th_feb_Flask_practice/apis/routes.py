from flask import jsonify , Blueprint , request
from flask_jwt_extended import  jwt_required , get_jwt_identity

from models.product import Product

from random import randint 
from extenstions import jwt
from extenstions import db 
from models.user import User
api = Blueprint('api' , __name__ )

@api.route('/homepage' , methods = ["GET"])
@jwt_required()
def gernerate():
    _id = get_jwt_identity()
    user = User.query.get(_id)
    # print(user.id , user.username , )
    if(user.admin == True):
        return jsonify({"message" : "success /homepage" , "user" : _id }),200 


        
    # print(user)
    return jsonify({"message" : "Not Authorized"}),401 
    
#===================================================================================================================

@api.route("/products",methods=['POST'])
def post_products(): 
    name = request.json['name']
    description = request.json['description'] 
    price = request.json['price']
    qty = request.json['qty']
    new_product = Product(name , description , price , qty)
    db.session.add(new_product) 
    db.session.commit()
    return jsonify({'name':name,'description':description , 'price':price ,'qty':qty}),200


@api.route('/products' , methods=['GET'])
@jwt_required()
def get_products():
    _id = get_jwt_identity()
    user = User.query.get(_id)
    # print(user.id , user.username , )
    if(user.admin == False):
        return jsonify({"message" : "Not authorized"  , "user" : _id }),200 
    allproducts = Product.query.all()
    def getdict(item):
        return {"id" : item.id , 'name' :item.name , 'description':item.description , 'price' :item.price , 'qty':item.qty} 
    # return jsonify(dir(allproducts))
    return jsonify( list(map(getdict , allproducts)))

@api.route('/products/<int:_id>' , methods=['GET'])
@jwt_required()
def get_product(_id):
    _id = get_jwt_identity()
    user = User.query.get(_id)
    # print(user.id , user.username , )
    if(user.admin == False):
        return jsonify({"message" : "Not authorized" , "user" : _id }),200 
    
    pro = Product.query.get( _id)
    
    return jsonify({"id" :pro.id,"name":pro.name,"desc":pro.description ,"price" :pro.price , "qty":pro.qty})



@api.route("/products/<int:_id>",methods=['PUT'])
@jwt_required()
def update_product(_id): 
    _id = get_jwt_identity()
    user = User.query.get(_id)
    # print(user.id , user.username , )
    if(user.admin == False):
        return jsonify({"message" : "Not authorized" , "user" : _id }),200 
    pro = Product.query.get(_id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    pro.name = name 
    pro.description = description 
    pro.price = price
    pro.qty  = qty 

    db.session.commit()
    return jsonify({'name':pro.name,'description':pro.description , 'price':pro.price ,'qty':pro.qty}),200


@api.route("/products/<int:_id>",methods=['DELETE'])
@jwt_required()
def delete_product(_id):
    u = get_jwt_identity()
    user = User.query.get(u)
    # print(user.id , user.username , )
    if(user.admin == False):
        return jsonify({"message" : "Not authorized" , "user" : u }),200 
    pro = Product.query.get(_id)
    db.session.delete(pro)
    db.session.commit() 
    return f"detleted {_id}" , 200