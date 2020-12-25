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

@app.route("/registery", methods=['POST'])
def register():
    data = request.values.to_dict()

    if len(data.keys()) != 2:
        return "requests is not valid"
    try:
        username ,password = data['username'],data['password']
    except:
        return "requests is not valid"
    
    if User.query.filter_by(username=username).first() is None:
        password = sha256(password.encode()+config.salt).hexdigest()
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return 'created now'
    return "username is exist"


@app.route("/set_data", methods=['POST'])
def set_data():
    data = request.values.to_dict()
    if len(data.keys()) != 3:
        return "requests is not valid"
    try:
        username ,password = data['username'],data['password']
    except:
        return "requests is not valid"
    if not check(username,password):
        return "invalid data"

    if Data.query.filter_by(username=username).first() is None:
        d = Data(enx_object = data['data'] ,username=username)
        db.session.add(d)
        db.session.commit()
        return 'set now'
    else:
        return "first you have to delete your last data"
    return {}

@app.route("/load_data", methods=['POST'])
def load():
    data = request.values.to_dict()
    if len(data.keys()) != 2:
        return "requests is not valid"
    try:
        username ,password = data['username'],data['password']
    except:
        return "requests is not valid"
    if not check(username,password):
        return "invalid data"

    data = Data.query.filter_by(username=username).first()
    if data is None:
        return "data is not exist"
    return data.enx_object


@app.route("/delete_data", methods=['POST'])
def delete_data():
    data = request.values.to_dict()
    if len(data.keys()) != 2:
        return "requests is not valid"
    try:
        username ,password = data['username'],data['password']
    except:
        return "requests is not valid"
    if not check(username,password):
        return "invalid data"
    d = Data.query.filter_by(username=username).first()
    if d is not None:
        d = db.session.query(Data).filter(Data.username==username).first()
        db.session.delete(d)
        db.session.commit()
        return 'delete now'
    else:
        return "first you have to add your data"
    return {}



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
