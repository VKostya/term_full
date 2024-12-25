from sqlalchemy import Column, Integer, String
from db.db_engine import Base


class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, unique=True, index=True)
    description = Column(String)
