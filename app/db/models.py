from sqlalchemy import Column, Integer, String
from db.db_engine import Base


class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, unique=True, index=True)
    description = Column(String)
    source = Column(String)


class TermLink(Base):
    __tablename__ = "term_links"

    id = Column(String, primary_key=True, index=True)
    parent_id = Column(Integer)
    child_id = Column(Integer)
    link_descr = Column(String)