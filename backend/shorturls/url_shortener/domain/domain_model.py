from pydantic import BaseModel

class UrlGetRequest(BaseModel):
    short_url: str

class UrlPostRequest(BaseModel):
    long_url: str


class UrlDomainModel(BaseModel):
    short_url: str
    long_url: str

