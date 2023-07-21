# app/main/routes.py
from flask import render_template, request , redirect ,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User
from app.main import main_bp,auth_bp
from app.extensions import db
from flask_login import login_user,logout_user,login_required,current_user


@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name = current_user.name)
##############################################################
@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')

@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # print(email,name,password)

    user = User.query.filter_by(email = email).first()

    if user:
        redirect('auth.signup')

    new_user = User(email=email,name=name,password= generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()



    return redirect(url_for('auth.login'))

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email = email).first()

    if not user or not check_password_hash(user.password,password):
        return redirect('auth.login')


  
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



