
from flask import Flask, url_for, redirect, render_template, request, flash
import csv

app = Flask(__name__)


# app.config['SECRET_KEY'] = 'This is my secret key'
# # app.config['MYSQL_HOST'] = 'localhost'
# # app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = ''
# # app.config['MYSQL_DB'] = 'flask'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hqnsnpalmqpsjj:b4360cf721f93e8077fd5e161840054b7ff1772fae0ffb9c05825425be73ed6d@ec2-34-231-42-166.compute-1.amazonaws.com:5432/dfivgdppfdth1r'


# class Submit(db.Model, UserMixin)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


def write_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('index.html')
        except:
            return 'Form not submitted'
    else:
        return 'try again'


if __name__ == "__main__":
    app.run()
