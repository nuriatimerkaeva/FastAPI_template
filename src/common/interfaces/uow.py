from sqlalchemy.orm import Session


class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def add(self, obj):
        self.session.add(obj)

    def remove(self, obj):
        self.session.remove(obj)
