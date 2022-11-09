from django.db import models

class SearchBox(models.Model):
    search_box = models.CharField(max_length=300)
    number = models.SmallIntegerField()

    def __str__(self):
        return self.search_box

class Search(models.Model):
    titles = models.CharField(max_length=255)
    urls = models.CharField(max_length=255)

    def __str__(self):
        return self.titles
