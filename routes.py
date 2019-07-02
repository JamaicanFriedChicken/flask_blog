from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app

posts = [
    {
        'author': 'Jirapat Kleepbua',
        'title': 'Blog Post 1',
        'content': 'I love Michael Lue and His FAT, too bad he isnt like Nick Young',
        'date_posted': 'June 22, 2019'
    },
    {
        'author': 'Ngimanita',
        'title': 'Blog Post 2',
        'content': 'I love P Toon!! and Fern my Side Chick',
        'date_posted': 'June 23,2019'
    },
    {
        'author': 'Moness',
        'title': 'Blog Post 3',
        'content': 'Michaeeeeeeeeel! Nine wants to go Hasong and Korean BBQ',
        'date_posted': 'June 25, 2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #f key is only available for python 3.6 & above
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
