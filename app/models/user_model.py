from .bases_model import BaseModel, db
from hashlib import md5


class User(BaseModel):
    __tablename__ = 'users'

    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def save_password(self, password_entry):
        hashed_password = md5(password_entry)
        self.password = hashed_password
        self.save(False)

    def compare_password(self, password):
        return self.password == md5(password)

    def __repr__(self):
        return '<Name %s>' % self.name
