#  Перевощиков Андрей 367472. Вариант 2
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'


@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        contact = Contact(name=name, phone=phone)
        db.session.add(contact)
        db.session.commit()
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/clear')
def clear():
    db.session.query(Contact).delete()
    db.session.commit()
    return '', 204


with app.app_context():
    db.create_all()

app.run()
