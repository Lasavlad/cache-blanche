from django.db import models
from core.models import CustomAuthorModel

class Author(models.Model):
    username = models.CharField(max_length=255)

    created_by = models.OneToOneField(
        CustomAuthorModel,
        related_name = 'author',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username