import logging

from sqlalchemy import distinct

from DB.models.base import Session, Base, engine
from DB.models.user import User
from DB.models.date import Date
from DB.models.receipt import Receipt

Base.metadata.create_all(engine)
session = Session()
logger = logging.getLogger()

def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            session.commit()
        except Exception as e:
            logger.error(e)
            session.rollback()
            return None

    persist.__name__ = func.__name__
    return persist


@db_persist
def add_user(chat_id, fullname=None, phone=None, pay_each_time=0):
    user = User(chat_id, fullname, phone, pay_each_time)
    session.add(user)


def get_user(chat_id):
    return session.query(User).filter(User.chat_id == chat_id).one_or_none()


@db_persist
def add_user_date(chat_id, day_of_week):

    user_date = Date(get_user(chat_id), day_of_week)
    session.add(user_date)


def get_all_user_most_pay_receipt(day_of_month):

    dates = session.query(Date).filter(Date.day_of_month == day_of_month).all()
    return [date.user for date in dates]


@db_persist
def add_user_receipt(chat_id, date,amount):
    user_receipt = Receipt(get_user(chat_id),date,amount)
    session.add(user_receipt)




