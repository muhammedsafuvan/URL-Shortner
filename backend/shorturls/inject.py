from url_shortener.inject import ShortUrlSubAppContainer

from dependency_injector import containers, providers

class ShortUrlContainer(containers.DeclarativeContainer):
    short_url = providers.Container(ShortUrlSubAppContainer)