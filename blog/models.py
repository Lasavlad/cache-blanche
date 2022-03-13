from django.db import models
from bloggers.models import Author

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
        Author,
        related_name='author_blogs',
        on_delete=models.CASCADE

    )
    date_of_post = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

class comments(models.Model):
    comment = models.CharField(max_length=255)
    blog = models.ForeignKey(
        Blog,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.comment[:30]