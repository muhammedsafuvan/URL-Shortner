from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class ShortUrlCreateViewTest(APITestCase):
    def setUp(self) -> None:
        self.api_url = reverse(
            "create_shorten_url",
        )

    def test_post(self):
        
        response = self.client.post(
            path=self.api_url,
            data={
                "long_url" : "https://www.abc.com"
            },
            format="json",
        )
        print("RES")
        print(response.json())

        # THEN assert that a 200 is returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)