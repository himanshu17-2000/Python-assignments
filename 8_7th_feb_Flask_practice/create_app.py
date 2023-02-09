from flask import Flask
import os


from apis.routes import api
from auth.routes import auth

from extenstions import jwt, db ,migrate

def createApp():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')if(os.getenv('JWT_SECRET'))else"omjaijagdhishivhare"
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(api, url_prefix='/api')
    return app