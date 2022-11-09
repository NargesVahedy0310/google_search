from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
import time
from googlesearch import search


class SearchView(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializers

class SearchBoxView(viewsets.ModelViewSet):
    queryset = SearchBox.objects.all()
    serializer_class = SearchBoxSerializers

    def post(self, request):
        return self.create(request)

    # def search_results(query, number, advanced=True):
    #     def __init__(self, urls, titles):
    #         self.urls = urls
    #         self.titles = titles
    #     titles = []
    #     urls = []
    #     for title in search(query, num_results=number, advanced=advanced):
    #         titles.append(title.title)
    #         urls.append(title.url)
    #         print(list(zip(titles, urls)))
    #
    # search_results(SearchBox.search_box,SearchBox.number)
    # time.sleep(10)


