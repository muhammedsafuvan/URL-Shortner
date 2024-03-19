from url_shortener.data.db_repo import ShortUrlDbRepository
from url_shortener.data.abstract_repo import ShortUrlAbstractRepository
from url_shortener.domain.usecases.create_short_url_usecase import CreateShortUrlUseCase
from url_shortener.domain.usecases.get_url_usecase import GetUrlUseCase

from dependency_injector import containers, providers


class ShortUrlSubAppContainer(containers.DeclarativeContainer):
    repo = providers.Dependency(
        instance_of=ShortUrlAbstractRepository,  # type: ignore[misc]
        default=ShortUrlDbRepository(),
    )

    get_url_usecase = providers.Factory(GetUrlUseCase)
    create_short_url_usecase = providers.Factory(CreateShortUrlUseCase)