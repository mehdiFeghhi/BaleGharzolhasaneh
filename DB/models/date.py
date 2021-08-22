from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from DB.models.base import Base


class Date(Base):
    __tablename__ = "dates"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User")
    day_of_month = Column(Integer)

    def __init__(self, user, day_of_month):
        self.user = user
        self.day_of_month = day_of_month


