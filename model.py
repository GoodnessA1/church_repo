from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class register(db.Model):
    __tablename__ = "prayer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(15))
    prayer_request = db.Column(db.Text)

def insert_all(x):
    add_details = register(name=x[0], email=x[1], phone_number=x[2], prayer_request=x[3])
    db.session.add(add_details)
    db.session.commit()
    print("<--Data added successfully-->")
    return (0)

def load_all():
    data = register.query.all()
    return (data)