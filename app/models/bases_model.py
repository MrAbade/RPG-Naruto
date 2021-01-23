from datetime import datetime, timezone

from app.configs.database import SingletonSQLAlchemy


db = SingletonSQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def before_save(self, *args, **kwargs):
        return

    def before_save(self, *args, **kwargs):
        return

    def save(self, commit=True):
        self.before_save()

        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error

        self.before_save()

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.delete(self)
