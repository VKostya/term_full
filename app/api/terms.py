from db.models import Term
from db.utils import get_db
from sqlalchemy.orm import Session
from models.term_models import TermCreate, Terms
from fastapi import HTTPException, Depends, APIRouter


term_router = APIRouter()


@term_router.post("/terms/", response_model=Terms)
def create_term(term: TermCreate, db: Session = Depends(get_db)):
    db_term = Term(**term.dict())
    try:
        db.add(db_term)
        db.commit()
        db.refresh(db_term)
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    return db_term


@term_router.get("/terms/", response_model=list[Terms])
def read_terms(db: Session = Depends(get_db)):
    try:
        terms = db.query(Term).all()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    return terms


@term_router.get("/terms/{id}", response_model=Terms)
def read_term(id: int, db: Session = Depends(get_db)):
    try:
        term = db.query(Term).filter(Term.id == id).first()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    if term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return term

@term_router.put("/terms/{id}", response_model=Terms)
def update_term(id: int, term: TermCreate, db: Session = Depends(get_db)):
    try:
        db_term = db.query(Term).filter(Term.id == id).first()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    for key, value in term.dict().items():
        setattr(db_term, key, value)
    db.commit()
    return db_term

@term_router.delete("/terms/{id}")
def delete_term(id: int, db: Session = Depends(get_db)):
    try:
        db_term = db.query(Term).filter(Term.id == id).first()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db.delete(db_term)
    db.commit()
    return {"message": "Term deleted successfully"}
