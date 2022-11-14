from django.db import models

class SearchBox(models.Model):
    title = models.CharField(max_length=300)
    number = models.SmallIntegerField()

    def __str__(self):
        return self.title

class ValueSearch(models.Model):
    titles = models.CharField(max_length=255000)
    urls = models.CharField(max_length=255000)

    def __str__(self):
        return self.titles
