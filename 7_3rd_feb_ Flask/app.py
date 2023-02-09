from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)
migrate.init_app(app,db)

 

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<id {self.username}>'

class Items(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

@app.route('/signup', methods=['POST'])
def signup():
    """
    Signup endpoint to create a new user
    returns: string
    """
    request_data = request.json
    username = request_data.get('username')
    password = request_data.get('password')

    if not username or not password:
        return {'error': 'Username and password are required'}, 400

    # user = User.query.filter_by(username=username).first()
    user = Users.query.filter_by(username=username).first()
    if user:
        return {'error': 'Username already exists'}, 400

    user = Users(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return {'message': 'User created successfully'}, 201


@app.route('/login' , methods= ['POST'])
def login():
    
    request_data = request.json
    username = request_data.get('username')
    password = request_data.get('password')
    user = Users.query.filter_by(username=username,password=password).first()
    if(user):
        return jsonify({'message': 'User logged in '}), 201
    else:
        return jsonify({'message': 'Authentication failed'}),400

@app.route("/alldata" , methods=['GET'])
def get_data():
    users = Users.query.all()
    def get_dict(item):
        return { "username": item.username , "password":item.password} 

    user = list(map(get_dict , users))
    print(user)
    
    return jsonify(user)

