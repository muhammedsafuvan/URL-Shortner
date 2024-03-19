from django.apps import AppConfig


class UrlShortenerConfig(AppConfig):
    name = 'short_urls'
    inject_container = None


    def ready(self):
        from backend.shorturls import url_shortener

        from backend.shorturls.inject import ShortUrlContainer
        from backend.shorturls.url_shortener.domain.usecases import create_short_url_usecase

        self.inject_container = ShortUrlContainer()
        self.inject_container.wire(
            packages=[
                url_shortener,
            ],
            modules=[
                # create_short_url_usecase,
            ],
        )

