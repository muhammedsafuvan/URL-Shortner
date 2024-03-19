
from typing import TYPE_CHECKING
from inject import ShortUrlSubAppContainer
# from ...inject import ShortUrlContainer
# from inject import ShortUrlContainer
from url_shortener.domain.domain_model import UrlGetRequest, UrlPostRequest
from url_shortener.domain.usecases.get_url_usecase import GetUrlUseCase
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponseRedirect
from dependency_injector.wiring import Provide, inject
from rest_framework.response import Response
from rest_framework import status
from url_shortener.domain.usecases.create_short_url_usecase import CreateShortUrlUseCase

# if TYPE_CHECKING:
    
class ShortUrlCreateView(APIView):

    # @inject
    def post(
        self,
        request: HttpRequest,
        # create_short_url_usecase=  CreateShortUrlUseCase()
        # create_short_url_usecase: "CreateShortUrlUseCase" = Provide[
        #     ShortUrlSubAppContainer.create_short_url_usecase
        #     # "short_url.create_short_url_usecase"
        # ],
    ):
        create_short_url_usecase = CreateShortUrlUseCase()

        print("REQ")
        print(request.__dict__)
        long_url = request.data.get('long_url')  
        print(long_url)
        create_request = UrlPostRequest(long_url=long_url)
        
        api_response = create_short_url_usecase.execute(create_request = create_request)
        print("RESPONSE")
        print(api_response)
        return Response(
            data=api_response, status=status.HTTP_201_CREATED
        )
    
class ShortUrlGetView(APIView):


    def get(
        self,
        request: HttpRequest,
        short_url: str,
        get_url_usecase: GetUrlUseCase = Provide[
            "short_url.get_url_usecase"
        ],
    ):
        get_request = UrlGetRequest(short_url=short_url)
        
        dm = get_url_usecase.execute(get_request = get_request)
        long_url = dm.long_url
        # Redirect to the long URL
        return HttpResponseRedirect(long_url)