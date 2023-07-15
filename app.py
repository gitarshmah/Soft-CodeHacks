from flask import render_template, session, Flask, redirect, url_for
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
@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)