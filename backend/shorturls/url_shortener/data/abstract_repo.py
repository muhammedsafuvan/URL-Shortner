
import abc

from backend.shorturls.url_shortener.domain.domain_model import UrlDomainModel, UrlGetRequest


class ShortUrlAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(
        self, request: UrlGetRequest
    ) -> UrlDomainModel:
        """Get a actual URL  by short url"""
        pass


    @abc.abstractmethod
    def create(self, url_dm: UrlDomainModel) -> UrlDomainModel:
        """Create a short URL from the request object."""
        pass