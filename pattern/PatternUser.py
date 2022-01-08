from pydantic import BaseModel


class PatternUserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class PatternUserSupport(BaseModel):
    url: str
    text: str


class PatternUser(BaseModel):
    data: PatternUserData
    support: PatternUserSupport


class PatternUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[PatternUserData]
    support: PatternUserSupport
