
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

import pickle
# Initialize the app
app = Flask(__name__,template_folder='templates')
app.secret_key = 'session_1234*'
model = pickle.load(open('model1.pkl', 'rb')) # loading the trained model


#Database configuration
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sai14@localhost:3306/session_register_user_details'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sai14@localhost:3306/session_register_user_details'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

#Routes
@app.route('/') # Homepage
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST']) # Login
def login():
    user = None
    if request.method=='POST':
        user_name=request.form['user_name']
        password=request.form['password']

     # Query the database for the user based on the provided username
        user = Users.query.filter_by(user_name=user_name).first()
    if user:

        if password == user.password:
            session['user_id'] = user.user_id
            return redirect(url_for('predict'))
        else:
            flash('Incorrect password. Please check your credentials.', 'error')

    else:
        flash('User not found. Please check your credentials.', 'error')
        return render_template('login.html')


@app.route('/register',methods=['GET','POST']) #Register
def register():
    if request.method=='POST':
        user_name=request.form['user_name']
        password=request.form['password']

        # Check if the username already exists in the database
        existing_user = Users.query.filter_by(user_name=user_name).first()

        if existing_user:
            flash('Username already exists. Please choose another username.', 'error')
        else:
            # Create a new user record in the database
            new_user = Users(user_name=user_name, password=password)
            db.session.add(new_user)
            db.session.commit()

        flash('Registration successful! You can now log in.', 'success')

        # Redirect the user to the login page after successful registration
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method =='POST':
        applicantincome = int(request.form['applicantincome'])
        coapplicantincome = float(request.form['coapplicantincome'])
        loanamount = float(request.form['loanamount'])
        loan_amount_term = float(request.form['loan_amount_term'])
        credit_history = float(request.form['credit_history'])
        gender = int(request.form['gender'])
        married = int(request.form['married'])
        dependents = int(request.form['dependents'])
        education = int(request.form['education'])
        self_employed = int(request.form['self_employed'])
        property_area = int(request.form['property_area'])

        prediction = model.predict(
            [[applicantincome,coapplicantincome , loanamount, loan_amount_term, credit_history,
              gender , married,dependents,education,self_employed,property_area]])
        output = round(float(prediction[0]),2)
        return render_template('predict.html', prediction_text='Congrats !! You are eligible for Loan'.format(output))

    return render_template('predict.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
