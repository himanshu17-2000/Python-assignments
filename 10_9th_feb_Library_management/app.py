from init_app import init_app 
from init_packages import db
app = init_app()

if(__name__ == "__main__"):
    app.run(debug=True)

