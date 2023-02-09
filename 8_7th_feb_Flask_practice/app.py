
from create_app import createApp
app =createApp()

@app.route("/",methods=['GET'])
def get_home(): 
    return "<h1> Himanshu Kumar amb </h1>"

if(__name__ == "__main__"):
    app.run(debug= True)


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///collections.sqlite"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')if(os.getenv('JWT_SECRET'))else"omjaijagdhishivhare"




# class Product(db.Model):
#     __tablename__ = "product"
#     id = db.Column(db.Integer , primary_key = True)
#     name = db.Column(db.String(100), unique=True )
#     description = db.Column(db.String(200))
#     price =db.Column(db.Float)
#     qty =db.Column(db.Integer)

#     def __init__(self , name , description, price ,qty):
#         self.name = name 
#         self.description = description
#         self.price = price 
#         self.qty = qty 



# class User(db.Model):
#     __tablename__ = "user"
#     id=db.Column(db.Integer , primary_key = True)
#     username = db.Column(db.String(50), unique=True , nullable = False) 
#     password = db.Column(db.String(50), nullable = False)
#     def __init__(self,username,password):
#         self.username = username 
#         self.password = password 

# @app.route("/",methods=['GET'])
# def get_home(): 
#     return "<h1> Himanshu Kumar amb </h1>"
#========================user signUp/signIn ============================

# @app.route("/register",methods=['POST'])
# def register_user():
#     username = request.json['username']
#     password = request.json['password']
#     new_user = User(username=username , password=password)
#     if(User.query.filter_by(username=username,password=password).first()):
#         return  {'error': 'Username already exists'},400 
    
#     db.session.add(new_user) 
#     db.session.commit()

#     return jsonify({'username':username , 'password':password}),200
# @app.route("/users",methods=['GET'])
# def all_users():
#     all_users = User.query.all() 
#     def get_dict(item):
#         return {"username" :item.username , "password" :item.password , "id" :item.id}

#     return jsonify(list(map(get_dict , all_users))),200

# @app.route('/login',methods=['POST'])
# def login_user():
#     username = request.json['username']
#     password = request.json['password']
#     if(User.query.filter_by(username=username,password=password).first()):
#         return  {'message' :'user logged in '} , 200 
    
#     return jsonify({'message' :'user not found  in database'})  , 400 


#======================== user signUp/signIn ^  ============================

