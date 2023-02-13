from flask import Flask 
from init_packages import db , migrate , jwt
from api.routes import api 
from flask_cors import CORS
from models import Members , Transactions , Books
def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['JWT_SECRET_KEY'] = "omjaijagdhishivhare"

    app.register_blueprint(api)
    CORS(app)
    db.init_app(app)
    migrate.init_app(app ,db)
    jwt.init_app(app)
    
    return app