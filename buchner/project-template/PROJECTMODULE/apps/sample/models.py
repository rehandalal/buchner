from sqlalchemy import Column, Integer

from PROJECTMODULE.database.classes import Model


class Sample(Model):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True, autoincrement=True)
