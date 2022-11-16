from django.db import models

class SearchBox(models.Model):
    title = models.CharField(max_length=300)
    number = models.SmallIntegerField()

    def __str__(self):
        return self.title

class ValueSearch(models.Model):
    title = models.TextField(max_length=1000)
    titles = models.TextField()
    urls = models.TextField()

    def __str__(self):
        return self.titles
