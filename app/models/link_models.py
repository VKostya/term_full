from pydantic import BaseModel


class TermLinksBase(BaseModel):
    parent_id: int
    child_id: int
    link_descr: str


class TermLinkCreate(TermLinksBase):
    pass


class TermLinks(TermLinksBase):
    id: str

    class Config:
        orm_mode = True
