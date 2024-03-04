from backend.shorturls.url_shortener.data.abstract_repo import ShortUrlAbstractRepository
from backend.shorturls.url_shortener.domain.domain_model import UrlsDomainModel, UrlsGetRequest
from backend.shorturls.url_shortener.models import Urls


class ShortUrlDbRepository(ShortUrlAbstractRepository):
    def get(
        self, request: UrlsGetRequest
    ) -> UrlsDomainModel:
        
        url_object = Urls.objects.filter(short_code=request.short_url).first()
        url_dm = UrlsDomainModel(
            short_url =url_object.short_code,
            long_url = url_object.original_url,
        )

        return url_dm