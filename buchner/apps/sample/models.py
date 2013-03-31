from buchner.database.classes import Model
from sqlalchemy import Column, Integer


class Sample(Model):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True, autoincrement=True)
