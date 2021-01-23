from .bases_model import BaseModel, db


class Ninja(BaseModel):
    __tablename__ = 'ninjas'

    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    life = db.Column(db.String, nullable=False)
    chakra = db.Column(db.String, nullable=False)

    village_id = db.Column(db.Integer, db.ForeignKey('villages.id'))

    def __repr__(self):
        return '<Name %s>' % self.name
