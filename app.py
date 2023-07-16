from flask import render_template, session, Flask, redirect, url_for,request
from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from impinfo import list_of_states, find_crop, find_secity
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

class infoform(FlaskForm):
    temperature = DecimalField('Temperature: ', validators=[DataRequired()])
    humidity = DecimalField('Humidity: ', validators=[DataRequired()])
    ph = DecimalField('Ph: ', validators=[DataRequired()])
    rainfall = DecimalField('Rainfall(mm): ', validators=[DataRequired()])
    ChooseState = SelectField("State: ", choices= list_of_states)
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email: ')
    password = StringField('Password: ')
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/main', methods=['GET', 'POST'])
def main():
    form = infoform()
    if form.validate_on_submit():
        session['temperature'] = form.temperature.data
        session['humidity'] = form.humidity.data
        session['ph'] = form.ph.data
        session['rainfall'] = form.rainfall.data
        session['ChooseState'] = form.ChooseState.data
       
        y = find_crop(float(form.temperature.data),float(form.humidity.data), float(form.ph.data),float(form.rainfall.data))
        session['find_crop']=str(y[0])
        session['find_secity'] = find_secity(str(y[0]),form.ChooseState.data)
        return redirect(url_for('answer'))
        
    return render_template('main.html',form=form)

    
@app.route('/answer')
def answer():
    return render_template('answer.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/success_log')
def success_log():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/success')
# def success():
#     return render_template('main.html')

@app.route('/success')
def success():
    form = LoginForm()
    if form.validate_on_submit():
         session['email'] = form.email.data
         session['password'] = form.password.data
    return redirect(url_for('main'))



if __name__ == '__main__':
    app.run(debug=True)