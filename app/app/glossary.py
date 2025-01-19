from db.utils import get_db
from fastapi import Depends, APIRouter, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from api.utils import read_all_terms, read_one_term, get_related_terms

templates = Jinja2Templates(directory="static")
glossary_router = APIRouter(include_in_schema=False)

@glossary_router.get("/terms/")
def home(request: Request, db: Session = Depends(get_db)):
    terms = read_all_terms(db=db)
    return templates.TemplateResponse(
        "glossary/main.html",
        {
            "request": request,
            "terms": terms
        }
    )
@glossary_router.get("/terms/{id}/")
def term_info(id: int, request: Request, db: Session = Depends(get_db)):
    term = read_one_term(id=id, db=db)  
    related_terms = get_related_terms(id=id, db=db)
    rel_flag = len(related_terms)

    return templates.TemplateResponse(
        "glossary/term.html",
        {
            "request": request,
            "term": term,
            "rel_flag": rel_flag,
            "related": related_terms
        }
    )

@glossary_router.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(
        "home_page.html",
        {
            "request": request
        }
    )