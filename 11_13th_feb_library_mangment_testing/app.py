from init_app import create_app
from sqlobject import *
import os
from models.Member import Member
from models.Transaction import Transaction
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
