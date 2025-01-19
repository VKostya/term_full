from db.utils import get_db
from fastapi import Depends, APIRouter, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="static")
mindmap_router = APIRouter(include_in_schema=False)

@mindmap_router.get("/mindmap/")
def home(request: Request, db: Session = Depends(get_db)):
    nodes = [
    {'id': 'Аллокация'},
    {'id': 'Оптимизация распределения данных в хранилище'},
    {'id': 'Шардирование'},
    {'id': 'Ключ шардирования'},
    {'id': 'Горизонтальное шардирование'},
    {'id': 'Вертикальное шардирование'}
]

    links = [
    {'source': 'Аллокация', 'target': 'Шардирование'},
    {'source': 'Оптимизация распределения данных в хранилище', 'target': 'Шардирование'},
    {'source': 'Шардирование', 'target': 'Ключ шардирования'},
    {'source': 'Шардирование', 'target': 'Горизонтальное шардирование'},
    {'source': 'Шардирование', 'target': 'Вертикальное шардирование'}
]
    return templates.TemplateResponse(
        "mindmap/main.html",
        {
            "request": request,
            "nodes": nodes,
            "links": links
        }
    )