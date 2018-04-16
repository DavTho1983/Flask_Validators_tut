from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import IntegerField, SelectField
from wtforms.validators import InputRequired
from perfect_numbers import classify, listInRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

class PerfectForm(Form):
    inputNumber = IntegerField('Input a number to see if it\'s abundant, perfect, or deficient', default=1, validators=[InputRequired(message='Please input an integer')])

class PerfectRangeForm(Form):
    startNumber = IntegerField('Input a type of aliquot number, a start number, an end number and an aliquot classification to see the numbers of that classification within that range', default=1, validators=[InputRequired(message='Please input an integer')])
    endNumber = IntegerField('input a number', default=1, validators=[InputRequired(message='Please input an integer')])
    aliquot = SelectField(
        'Aliquot classification',
        choices=[('abundant', 'abundant'), ('perfect', 'perfect'), ('deficient', 'deficient')],
        default='abundant'
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = PerfectForm(request.form, prefix="form1")
    form2 = PerfectRangeForm(request.form, prefix="form2")
    num = 1
    startNumber = 1
    endNumber = 1
    aliquot = 'abundant'
    Classify = classify(num)
    ListInRange = listInRange(startNumber, endNumber, aliquot)
    if form1.validate_on_submit():
        num = form1.inputNumber.data
        Classify = classify(num)
        return render_template('index.html', num=num, form1=form1, form2=form2, startNumber=startNumber, endNumber=endNumber, aliquot=aliquot, classify=Classify, listInRange=ListInRange)
    return render_template('index.html', num=1, form1=form1, form2=form2, startNumber=1, endNumber=1, aliquot=aliquot, classify=Classify, listInRange=ListInRange)

@app.route('/aliRange', methods=['GET', 'POST'])
def aliRange():
    form1 = PerfectForm(request.form, prefix="form1")
    form2 = PerfectRangeForm(request.form, prefix="form2")
    num = 1
    startNumber = form2.startNumber.data
    endNumber = form2.endNumber.data
    aliquot = 'abundant'
    Classify = classify(num)
    ListInRange = listInRange(1, 1, 'abundant')
    print(ListInRange)
    if form2.validate_on_submit():
        startNumber = form2.startNumber.data
        endNumber = form2.endNumber.data
        aliquot = form2.aliquot.data
        ListInRange = listInRange(startNumber, endNumber, aliquot)
        return render_template('index.html', num=num, form1=form1, form2=form2, startNumber=startNumber, endNumber=endNumber, aliquot=aliquot, classify=Classify, listInRange=ListInRange)
    return render_template('index.html', num=num, form1=form1, form2=form2, startNumber=1, endNumber=1, aliquot='abundant', classify=Classify, listInRange=ListInRange)

if __name__ == '__main__':
    app.run(debug=True)
