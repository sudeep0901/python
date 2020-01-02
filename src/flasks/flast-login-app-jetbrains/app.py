from flask import Flask, render_template,   redirect, url_for, request
from flask_login import  LoginManager
from flask_login import login_required, login_user, logout_user
import flask
from mockhelper import MockHelper as DBHelper
from passwordhelper import PasswordHelper
from WTFRegistration import  RegistrationForm
from user import User
print("welcome to flask app")

app = Flask(__name__)
login_manager = LoginManager(app)
print(dir(app))

DB = DBHelper()
PH = PasswordHelper()
app.secret_key = 'tPXJY3X37Qybz4QykV+hOyUxVQeEXf1Ao2C8upz+fGQXKsM'


@app.route("/")
# @login_required
def home():
    # return "Hello Welcome to Flask"
    registrationform = RegistrationForm()
    print(registrationform)

    # return render_template("home.html")

    return render_template("register.html", registrationform=registrationform)


@app.route("/account")
@login_required
def account():
    return "you are logged in"


@app.route("/login", methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)

    if stored_user and PH.validate_password(password, stored_user['email'], stored_user['hashed']):
        print(stored_user)
        user = User(email)
        login_user(user, remember=True)
    # user_password = DB.get_user(email)
    # if user_password and user_password == password:
    #     user = User(email)
    #     print(user)
    #     login_user(user)
        return redirect(url_for('account'))
    return home()


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register", methods=['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return render_template('register.html')

    print(request)
    email = request.form.get('email')
    pw1 = request.form.get('password')
    pw2 = request.form.get('password2')

    if not pw1 == pw2:
        return redirect(url_for('home'))

    salt = PH.get_salt()
    print(salt)
    hashed = PH.get_hash(pw1 + salt)
    print(hashed)
    DB.add_user(email, salt, hashed)
    return redirect(url_for('home'))


app.run(port=5000, debug=True)