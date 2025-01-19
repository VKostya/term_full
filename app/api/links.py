from db.models import TermLink
from db.utils import get_db
from sqlalchemy.orm import Session
from models.link_models import TermLinkCreate, TermLinks
from fastapi import HTTPException, Depends, APIRouter


link_router = APIRouter()


@link_router.post("/links/", response_model=TermLinks)
def create_term(term_link: TermLinkCreate, db: Session = Depends(get_db)):
    try:
        db_term_link = TermLink(**term_link.dict())
        db_term_link.id = str(term_link.parent_id) + '-' + str(term_link.child_id)
        db.add(db_term_link)
        db.commit()
        db.refresh(db_term_link)
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    return db_term_link


@link_router.get("/links/", response_model=list[TermLinks])
def read_terms(db: Session = Depends(get_db)):
    try:
        term_links = db.query(TermLink).all()
    except:
        raise HTTPException(status_code=502, detail="DB error")    
    return term_links


@link_router.put("/links/{pid}/{cid}/", response_model=TermLinks)
def update_term(pid: int, cid: int, term_link: TermLinkCreate, db: Session = Depends(get_db)):
    try:
        db_term_link = db.query(TermLink).filter(TermLink.parent_id == pid, TermLink.child_id == cid).first()
    except:
        raise HTTPException(status_code=502, detail="DB error")   
    if db_term_link is None:
        raise HTTPException(status_code=404, detail="Term not found")
    for key, value in term_link.dict().items():
        setattr(db_term_link, key, value)
    db.commit()
    return db_term_link


@link_router.delete("/links/{pid}/{cid}/")
def delete_term(pid: int, cid: int, db: Session = Depends(get_db)):
    try:
        db_term_link = db.query(TermLink).filter(TermLink.parent_id == pid, TermLink.child_id == cid).first()
    except:
        raise HTTPException(status_code=502, detail="DB error")   
    if db_term_link is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db.delete(db_term_link)
    db.commit()
    return {"message": "TermLink deleted successfully"}
