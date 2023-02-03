from flask import render_template, url_for, flash, redirect, request
from init import app, db, bcrypt
from forms import RegistrationForm, LoginForm, ContactForm, Contact2Form
from models import User, Post, Contact, Contact2


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def test():
    return redirect("https://docs.google.com/document/d/1-liOIVfufhk2B8u3YQ6yRAjkR8CrJu-2-jrJwyL6WoI/edit?usp=sharing")

@app.route("/construction")
def construction():
    return render_template('construction.html', title='EECS281')

@app.route("/construction2")
def construction2():
    return render_template('construction2.html', title='EECS370')
@app.route("/underconstruction")
def construction3():
    return render_template('underconstruction.html', title='EECS370')
@app.route("/stock")
def stock():
    return render_template('stock.html', title='stock')


@app.route('/contact',methods=['GET','POST'])
def contact():
  form = ContactForm()

  if form.validate_on_submit():
        user = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you! I will contact you soon!', 'success')
        
        return redirect(url_for('home'))
  return render_template('contact.html', form=form)

@app.route("/contact2",methods=['GET','POST'])
def index():
  form = Contact2Form()

  if form.validate_on_submit():
        user = Contact2(name=form.name.data, email=form.email.data, project_choice=form.project_choice.data, Agree = form.Agree.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you! I will contact you soon!', 'success')
        
        return redirect(url_for('home'))
  return render_template('contact2.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)