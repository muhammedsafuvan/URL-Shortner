
import abc

from url_shortener.domain.domain_model import UrlDomainModel, UrlGetRequest


class ShortUrlAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(
        self, request: UrlGetRequest
    ) -> UrlDomainModel:
        """Get a actual URL  by short url"""
        pass


    @abc.abstractmethod
    def create(self, request: UrlDomainModel) -> UrlDomainModel:
        """Create a short URL from the request object."""
        pass