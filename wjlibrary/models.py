from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    fullName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.fullName


class World(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
