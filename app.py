from flask import Flask, render_template, flash, request, redirect, url_for, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
from main import attendance
from parse import * # only for dashboard
from jinja2 import Template
import numpy as np


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
final =[[] for i in range(8)]

class LoginForm(Form):
		Reg_No = TextField('Name:', validators=[validators.required()])
		Password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
@app.route("/",methods=['GET', 'POST'])
def index():
	form = LoginForm(request.form)
	# print form.errors
	if request.method == 'POST':
		session['username']=request.form['Reg_No']
		session['password']=request.form['Password']
	
		if form.validate():
			# Save the comment here.
			username=session['username']
			password=session['password']
			final = attendance(username,password)
			finals=np.asarray(final)
			finals=finals.T
			leng=len(final[0])
			return render_template('dashboard.html', resultsT = finals, results = final, regno=username, length=leng)
			# return redirect(url_for('atten', arg = final))
		else:
			flash('Error: All the form fields are required. ')
		
    
	return render_template('index.html', form=form)

@app.route("/dashboard")
def dashboard():
	regno=session['username']
	filename=regno+"_attendance.html"
	final = parseatt(filename)
	finals=np.asarray(final)
	finals=finals.T
	leng=len(final[0])
	return render_template('dashboard.html', resultsT = finals, results = final, regno=regno, length=leng)

@app.route("/timetable")
def timetable():
	return render_template('timetable.html')

@app.route("/marks")
def marks():
	return render_template('marks.html')

@app.route("/history")
def history():
	regno=session['username']
	filename=regno+"_history.html"
	history,credits=parsehistory(filename)
	finals_hist=np.asarray(history)
	finals_hist=finals_hist.T
	# finals_credits=np.asarray(credits)
	# finals_credits=finals_credits.T
	return render_template('history.html', regno=regno, history=finals_hist, credits=credits)

@app.route("/plan")
def plan():
	regno=session['username']
	return render_template('timetable_gen.html', regno=regno)

if __name__ == "__main__":
	app.run()
