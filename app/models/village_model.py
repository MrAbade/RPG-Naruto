from .bases_model import BaseModel, db


class Village(BaseModel):
    __tablename__ = 'villages'

    name = db.Column(db.String, nullable=False, unique=True)

    ninjas = db.relationship('Ninja', backref=db.backref('villages'))

    def __repr__(self):
        return '<Village %s>' % self.name
