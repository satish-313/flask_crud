from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<candidate %r>' % self.username

# run in python shell
# >>> from app import db
# >>> db.create_all()
# >>> from app import candidate
# >>> admin = candidate(username="admin",email="admin@gmail.com")
# >>> guest = candidate(username="guest",email="guest@gmail.com")
# >>> db.session.add(admin)
# >>> db.session.add(guest)
# >>> db.session.commit()
# >>> candidate.query.all()


@app.route('/')
def main():
    db.
    return 'Hello World!'

# @app.route('/all_candidate')
# def 