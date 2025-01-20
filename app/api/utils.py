from db.models import Term, TermLink
from fastapi import HTTPException


def read_all_terms(db):
    try:
        terms = db.query(Term).all()
    except:
        raise HTTPException(status_code=502, detail="DB error")
    return terms

def read_one_term(id, db):
    try:
        term = db.query(Term).filter(Term.id == id).first()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    if term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return term

def read_all_links(db):
    try:
        term_links = db.query(TermLink).all()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    return term_links

def get_related_terms(id, db):
    try:
        terms = db.query(Term).join(TermLink, Term.id == TermLink.child_id).filter(TermLink.parent_id == id).all()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    return terms

