from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json
from .models import *
from .serializers import *
import time
from googlesearch import search

class A(ModelViewSet):
    serializer_class = ValueSearch

    def get_queryset(self):
        return ValueSearch.objects.all()



class B(ModelViewSet):
    serializer_class = SearchBoxSerializers

    def get_queryset(self):
        return SearchBox.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = SearchBoxSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        # print(serializer)
        print("==")
        data_search = SearchBox.objects.all().values()
        last_data = data_search[::-1][0]
        data_title = last_data['title']
        data_num = last_data['number']
        def search_results(query, number, advanced=True):
            titles = []
            urls = []
            for title in search(query, num_results=number, advanced=advanced):
                titles.append(title.title)
                urls.append(title.url)
                print(list(zip(titles, urls)))
                print(len(urls), '   ', len(titles))
            data = {'titles': titles, 'urls': urls}
            print(data)
            serializer = ValueSearch(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data
            serializer.save()
            print('------', serializer)
        search_results(data_title, data_num-1)
        time.sleep(5)
        return Response(serializer.data)

class SearchListView(generics.ListCreateAPIView):
    queryset = ValueSearch.objects.all()
    serializer_class = ValueSearchSerializers