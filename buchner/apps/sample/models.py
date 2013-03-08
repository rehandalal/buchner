from buchner.database import Base
from sqlalchemy import Column, Integer

class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True, autoincrement=True)