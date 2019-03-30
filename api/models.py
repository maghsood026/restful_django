from django.db import models
from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
