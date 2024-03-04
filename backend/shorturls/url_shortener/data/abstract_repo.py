
import abc

from backend.shorturls.url_shortener.domain.domain_model import UrlsDomainModel, UrlsGetRequest


class ShortUrlAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(
        self, request: UrlsGetRequest
    ) -> UrlsDomainModel:
        """Get a actual URL  by short url"""
        pass


    @abc.abstractmethod
    def create(self, url_dm: UrlsDomainModel) -> UrlsDomainModel:
        """Create a short URL from the request object."""
        pass