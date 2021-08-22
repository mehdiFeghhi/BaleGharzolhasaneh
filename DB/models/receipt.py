from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, Date
from sqlalchemy.orm import relationship, backref
from DB.models.base import Base


class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    date = Column(Date)
    amount = Column(String)

    def __init__(self, user, date, amount):
        self.user = user
        self.date = date
        self.amount = amount
