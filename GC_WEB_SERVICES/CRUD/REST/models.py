from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
