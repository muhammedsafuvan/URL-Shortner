
from url_shortener.data.abstract_repo import ShortUrlAbstractRepository
from url_shortener.domain.domain_model import UrlDomainModel, UrlPostRequest
from dependency_injector.wiring import Provide


class CreateShortUrlUseCase:
    def __init__(
        self,
        url_repo: ShortUrlAbstractRepository = Provide["clickwrap.repo"],
    ):
        self.repo = url_repo

    def execute(self, create_request: UrlPostRequest ) -> UrlDomainModel :
        dm = self.repo.create(request=create_request)
        return dm