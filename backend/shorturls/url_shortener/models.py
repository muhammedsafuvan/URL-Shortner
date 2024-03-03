from django.db import models


class Urls(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
