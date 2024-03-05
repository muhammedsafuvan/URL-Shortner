
from inject import ShortUrlContainer
from url_shortener.domain.domain_model import UrlGetRequest, UrlPostRequest
from url_shortener.domain.usecases.create_short_url_usecase import CreateShortUrlUseCase
from url_shortener.domain.usecases.get_url_usecase import GetUrlUseCase
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponseRedirect
from dependency_injector.wiring import Provide
from rest_framework.response import Response
from rest_framework import status

class ShortUrlCreateView(APIView):

    def post(
        self,
        request: HttpRequest,
        long_url: str,
        create_short_url_usecase: CreateShortUrlUseCase = Provide[
            ShortUrlContainer.short_url.create_short_url_usecase
        ],
    ):
        create_request = UrlPostRequest(long_url=long_url)
        
        api_response = create_short_url_usecase.execute(create_request = create_request)
        return Response(
            data=api_response.dict_serialized(), status=status.HTTP_201_CREATED
        )
    
class ShortUrlGetView(APIView):


    def get(
        self,
        request: HttpRequest,
        short_url: str,
        get_url_usecase: GetUrlUseCase = Provide[
            ShortUrlContainer.short_url.get_url_usecase
        ],
    ):
        get_request = UrlGetRequest(short_url=short_url)
        
        dm = get_url_usecase.execute(get_request = get_request)
        long_url = dm.long_url
        # Redirect to the long URL
        return HttpResponseRedirect(long_url)