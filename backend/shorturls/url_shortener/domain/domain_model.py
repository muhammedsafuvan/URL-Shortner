from pydantic import BaseModel

class UrlsGetRequest(BaseModel):
    short_url: str


class UrlsDomainModel(BaseModel):
    short_url: str
    long_url: str

