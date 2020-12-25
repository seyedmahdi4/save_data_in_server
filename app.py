from flask import Flask, request, json
from models import *
import config

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

#@app.route("/login", methods=['POST'])

def login():
    usr ,pas = request.values.getlist('user') , request.values.getlist('passwd')
    return {}

@app.errorhandler(404)
def page_not_found(e):
    return '404 error', 404

def loao(Room):
    messages = History.query.filter_by(room=Room)

def save(data):
        message = History(username=username, message=msg.encode(
            'latin-1').decode('utf-8'), time_stamp=time_stamp, room=room, enc_key=enc_key)
        db.session.add(message)
        db.session.commit()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # 9055 ssl_context='adhoc'
