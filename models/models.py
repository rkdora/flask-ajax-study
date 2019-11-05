from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class LogContent(Base):
    __tablename__ = 'logcontents'
    id = Column(Integer, primary_key=True)
    log = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, log=None, date=None):
        self.log = log
        self.date = date

    def __repr__(self):
        return '<Log %r>' % (self.log)
