from sqlalchemy import Column, Integer, ForeignKey
from models.user import User

class Admin(User):
    __tablename__ = "admin"
    id = Column(Integer, ForeignKey('users.id'), primary_key=True, index=True)

    __mapper_args__ = {
        'polymorphic_identity':"A",
    }

    def __repr__(self):
        return "<User {0}>".format(self.username)