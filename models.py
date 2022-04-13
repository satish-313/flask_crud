from app import db

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(266), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self,title,year,description):
        self.title = title
        self.year = year
        self.description = description
    
    def __repr__(self):
        return f"id : ${self.id} , title : ${self.title}"
