
from url_shortener.data.db_repo import ShortUrlDbRepository
from url_shortener.data.abstract_repo import ShortUrlAbstractRepository
from url_shortener.domain.domain_model import UrlDomainModel, UrlPostRequest
from dependency_injector.wiring import Provide


class CreateShortUrlUseCase:
    # def __init__(
    #     self,
    #     url_repo: ShortUrlAbstractRepository = Provide["short_url.repo"],
    # ):
    #     self.repo = url_repo

    def execute(self, create_request: UrlPostRequest ) -> str :
        url_repo = ShortUrlDbRepository()
        dm = url_repo.create(request=create_request)
        url = 'http://127.0.0.1:8000/api/tinyurl/post/' + dm.short_url
        return url