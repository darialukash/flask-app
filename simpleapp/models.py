from simpleapp import db


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<Person: {}>'.format(self.name)

    def save(self):
        db.session.add(self)
