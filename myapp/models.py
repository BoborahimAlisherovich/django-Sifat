from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Article/image")
    create_data = models.DateTimeField(auto_now=True)
    #4ta maydon qo'shish
    def __str__(self) -> str:
        return f"{self.title}"

class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=3)

    article = models.ForeignKey(Article,on_delete=models.CASCADE)