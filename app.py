from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
from main import attendance
from jinja2 import Template


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
final =[[] for i in xrange(8)]

class LoginForm(Form):
		Reg_No = TextField('Name:', validators=[validators.required()])
		Password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
@app.route("/",methods=['GET', 'POST'])
def index():
	form = LoginForm(request.form)
	print form.errors
	if request.method == 'POST':
		username=request.form['Reg_No']
		password=request.form['Password']
	
		if form.validate():
			# Save the comment here.
			flash('Complete')
			final = attendance(username,password)
			return render_template('result.html', results = final)
			# return redirect(url_for('atten', arg = final))
		else:
			flash('Error: All the form fields are required. ')
	
	return render_template('index.html', form=form)

# @app.route("/att/<arg>")
# def atten(arg):
# 	return render_template('result.html', results = arg)

if __name__ == "__main__":
	app.run(port=8082)