from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class World(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=False)
    history_overview = models.TextField(null=True)
    purpose = models.TextField(null=True)

    def __str__(self):
        return self.title


class EnvironmentVariable(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=12)
    magnitude = models.DecimalField(max_digits=20, decimal_places=8)
    content = models.CharField(max_length=20)
