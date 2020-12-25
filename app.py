from flask import Flask, request, json
from models import *
import config
from hashlib import sha256

# Configure app
app = Flask(__name__)
app.secret_key = config.secret_key

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#@app.route("/", methods=['GET', 'POST'])
#def index():
#    return True

@app.route("/registery", methods=['POST'])
def register(): 
    try:
        username ,password = request.values.getlist('username')[0],request.values.getlist('password')[0]
    except:
        return "requests is not valid"
    u = User.query.filter_by(username=username).first()
    if u is None:
        password = sha256(password.encode()+config.salt).hexdigest()
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return 'created now'
    return "username is exist"
    
def check(username,password):
    password = sha256(password.encode()+config.salt).hexdigest()
    user = User.query.filter_by(username=username).first()
    if user.password == password:
        return True
    return False

@app.errorhandler(404)
def page_not_found(e):
    return '404 error', 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # 9055 ssl_context='adhoc'
