from flask import Flask ,request ,jsonify
from flask_sqlalchemy import SQLAlchemy
import os 
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///collections.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')

db = SQLAlchemy()
jwt = JWTManager(app)
db.init_app(app)

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100), unique=True )
    description = db.Column(db.String(200))
    price =db.Column(db.Float)
    qty =db.Column(db.Integer)

    def __init__(self , name , description, price ,qty):
        self.name = name 
        self.description = description
        self.price = price 
        self.qty = qty 



class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), unique=True , nullable = False) 
    password = db.Column(db.String(50), nullable = False)
    def __init__(self,username,password):
        self.username = username 
        self.password = password 

@app.route("/",methods=['GET'])
def get_home(): 
    return "<h1> Himanshu Kumar amb </h1>"
#========================user signUp/signIn ============================

@app.route("/register",methods=['POST'])
def register_user():
    username = request.json['username']
    password = request.json['password']
    new_user = User(username=username , password=password)
    if(User.query.filter_by(username=username,password=password).first()):
        return  {'error': 'Username already exists'},400 
    
    db.session.add(new_user) 
    db.session.commit()

    return jsonify({'username':username , 'password':password}),200
@app.route("/users",methods=['GET'])
def all_users():
    all_users = User.query.all() 
    def get_dict(item):
        return {"username" :item.username , "password" :item.password , "id" :item.id}

    return jsonify(list(map(get_dict , all_users))),200

@app.route('/login',methods=['POST'])
def login_user():
    username = request.json['username']
    password = request.json['password']
    if(User.query.filter_by(username=username,password=password).first()):
        return  {'message' :'user logged in '} , 200 
    
    return jsonify({'message' :'user not found  in database'})  , 400 


#======================== user signUp/signIn ^  ============================




@app.route("/products",methods=['POST'])
def post_products(): 
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    new_product = Product(name , description , price , qty)
    db.session.add(new_product) 
    db.session.commit()
    return jsonify({'name':name,'description':description , 'price':price ,'qty':qty}),200


@app.route('/products' , methods=['GET'])
def get_products():
    allproducts = Product.query.all()
    def getdict(item):
        return {"id" : item.id , 'name' :item.name , 'description':item.description , 'price' :item.price , 'qty':item.qty} 
    # return jsonify(dir(allproducts))
    return jsonify( list(map(getdict , allproducts)))

@app.route('/products/<int:_id>' , methods=['GET'])
def get_product(_id):
    pro = Product.query.get( _id)
    
    return jsonify({"id" :pro.id,"name":pro.name,"desc":pro.description ,"price" :pro.price , "qty":pro.qty})



@app.route("/products/<int:_id>",methods=['PUT'])
def update_product(_id): 
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


@app.route("/products/<int:_id>",methods=['DELETE'])
def delete_product(_id):
    pro = Product.query.get(_id)
    db.session.delete(pro)
    db.session.commit() 
    return "detleted" , 200

if(__name__ == "__main__"):
    app.run(debug= True)
