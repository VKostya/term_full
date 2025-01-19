from pydantic import BaseModel


class TermBase(BaseModel):
    keyword: str
    description: str
    source: str


class TermCreate(TermBase):
    pass


class Terms(TermBase):
    id: int

    class Config:
        orm_mode = True
