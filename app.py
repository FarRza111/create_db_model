import os
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, redirect


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer)
    customer_id = db.Column(db.String(100), unique = True, nullable = False)
    workplace = db.Column(db.String, nullable = False)
    private_info = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Student {self.firstname}'


@app.route('/')
def index():
    customers = Customer.query.all()
    return render_template('index.html', customers = customers)


if __name__ =="__main__":
    app.run(debug=True)
