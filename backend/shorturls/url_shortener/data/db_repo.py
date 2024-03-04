from backend.shorturls.url_shortener.data.abstract_repo import ShortUrlAbstractRepository
from backend.shorturls.url_shortener.domain.domain_model import UrlDomainModel, UrlGetRequest, UrlPostRequest
from backend.shorturls.url_shortener.models import Url
from datetime import datetime

import hashlib

class ShortUrlDbRepository(ShortUrlAbstractRepository):
    def get(
        self, request: UrlGetRequest
    ) -> UrlDomainModel:
        
        url_object = Url.objects.filter(short_code=request.short_url).first()
        url_dm = UrlDomainModel(
            short_url =url_object.short_code,
            long_url = url_object.original_url,
        )

        return url_dm
    
    def create(self, request: UrlPostRequest) -> UrlDomainModel:

        short_code = self.generate_short_url(request.long_url)

        url_object = Url.objects.create(short_code=short_code, original_url=request.long_url, created_at=datetime.now(),)
        url_dm = UrlDomainModel(
            short_url =url_object.short_code,
            long_url = url_object.original_url,
        )

        return url_dm
    

    def generate_short_url(self, long_url):
        # Use hashlib to create a hash value of the long URL
        hash_object = hashlib.sha1(long_url.encode())
        hex_dig = hash_object.hexdigest()

        # Take the first 8 characters of the hash and use them as the short URL
        short_url = hex_dig[:8]
        
        return short_url



