from flask import Flask, render_template, jsonify, redirect, flash, request, url_for
import flask
import flask_login
from flask_login import current_user, login_user, logout_user
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash
from src.types import User
from src import db
import logging


# configuration
DEBUG = True
BCRYPT_LOG_ROUNDS = 12

# instantiate the app
app = Flask(__name__,
            static_folder='./client/dist/static',
            template_folder='./client/dist')
app.config.from_object(__name__)
CORS(app, support_credentials=True)

app.secret_key = '47ad6df8-c40c-469b-a722-d14b0a18577c'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)


def hash_pwd(pwd):
    return bcrypt.generate_password_hash(pwd, BCRYPT_LOG_ROUNDS)

# class User(flask_login.UserMixin):
#     def __init__(self, email):
#         self.id = email

def get_users(reload=False):
    global users
    if reload or ('users' not in globals()):
        users = db.get_users()
    return users

@login_manager.user_loader
def user_loader(id):
    user = db.get_user(id)
    logging.debug(f'user loader for {id}: {user}')
    if user is not None:
        return User(**user)


@login_manager.request_loader
def request_loader(request):
    email, id, password = [request.form.get(e) for e in ['email', 'id', 'password']]    
    
    user = user_loader(id)
    logging.info(str(user))
    logging.info(type(user))
    
    if user is not None:
        logging.info("----------------")
        logging.info(db.get_user(id)['password'])
        logging.info(request.form['password'])
        logging.info(hash_pwd(request.form['password']))
        
        if bcrypt.check_password_hash(
            db.get_user(id)['password'],
            request.form['password']
        ):
            logging.debug(f'{id} is authenticated')
            return user


# @app.route('/login', methods=['POST'])
# def login():

@app.route('/log-check', methods=['GET'])
def log_check():
    print('checking if logged')
    
    if current_user.is_authenticated:
        return jsonify(current_user)
    else:
        return jsonify(None)

        

@app.route("/logout")
@cross_origin()
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    print('login')
    logout_user()
    
    id, password = [request.get_json()[e] for e in ['id', 'password']]
    logging.info(f'---> extracted: {id}, {password}')
    
    if current_user.is_authenticated:
        logging.info(f'already authenticated as {current_user}')
        return jsonify('ok'), 200 ## redirect(flask.url_for('index'))
    print("getting user info")
    
    user = db.get_user(id)
    
    chck = None if user is None else bcrypt.check_password_hash(
            user['password'],password)
    # logging.info(f'Check password: {chck}')
    if not chck:
            logging.info("invalid credentials")
            return jsonify("invalid credentials"), 401## redirect(flask.url_for('login'))

    login_user(User(**user) , remember=True)
    return jsonify('ok'), 200 ## redirect(flask.url_for('index'))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(str(db.get_users()))
    app.run(host="0.0.0.0")
    
