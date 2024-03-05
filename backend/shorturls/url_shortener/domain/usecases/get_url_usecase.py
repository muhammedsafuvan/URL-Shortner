
from url_shortener.data.abstract_repo import ShortUrlAbstractRepository
from url_shortener.domain.domain_model import UrlDomainModel, UrlGetRequest
from dependency_injector.wiring import Provide


class GetUrlUseCase:
    def __init__(
        self,
        url_repo: ShortUrlAbstractRepository = Provide["clickwrap.repo"],
    ):
        self.repo = url_repo

    def execute(self, get_request: UrlGetRequest ) -> UrlDomainModel:
        dm = self.repo.get(request=get_request)
        return dm