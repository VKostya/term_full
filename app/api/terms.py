from db.models import Term
from db.utils import get_db
from sqlalchemy.orm import Session
from models.term_models import TermCreate, Terms
from fastapi import HTTPException, Depends, APIRouter


router = APIRouter()


@router.post("/terms/", response_model=Terms)
def create_term(term: TermCreate, db: Session = Depends(get_db)):
    db_term = Term(**term.dict())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term


@router.get("/terms/", response_model=list[Terms])
def read_terms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    terms = db.query(Term).all()
    if limit <= skip:
        return terms
    return terms[skip:limit]


@router.get("/terms/{keyword}", response_model=Terms)
def read_term(keyword: str, db: Session = Depends(get_db)):
    term = db.query(Term).filter(Term.keyword == keyword).first()
    if term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return term


@router.put("/terms/{keyword}", response_model=Terms)
def update_term(keyword: str, term: TermCreate, db: Session = Depends(get_db)):
    db_term = db.query(Term).filter(Term.keyword == keyword).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    for key, value in term.dict().items():
        setattr(db_term, key, value)
    db.commit()
    return db_term


@router.delete("/terms/{keyword}")
def delete_term(keyword: str, db: Session = Depends(get_db)):
    db_term = db.query(Term).filter(Term.keyword == keyword).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db.delete(db_term)
    db.commit()
    return {"message": "Term deleted successfully"}
