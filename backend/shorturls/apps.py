from django.apps import AppConfig




class UrlShortenerConfig(AppConfig):
    name = 'short_urls'
    inject_container = None


    def ready(self):
        from backend.shorturls import url_shortener

        from backend.shorturls.inject import ShortUrlContainer

        self.inject_container = ShortUrlContainer()
        self.inject_container.wire(
            packages=[
                url_shortener,
            ],
            modules=[],
        )

