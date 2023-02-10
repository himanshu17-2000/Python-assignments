from flask import Flask 
from init_packages import db , migrate , jwt
from api.routes import api 
def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['JWT_SECRET_KEY'] = "omjaijagdhishivhare"

    app.register_blueprint(api)
    
    db.init_app(app)
    migrate.init_app(app ,db)
    jwt.init_app(app)
    return app