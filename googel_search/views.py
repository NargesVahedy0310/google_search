from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
import time
from googlesearch import search

class GoogelSearchAPI(ModelViewSet):
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
            data = {'titles': str(titles), 'urls': str(urls)}

            serializer = ValueSearchSerializers(data=data)
            print(type(serializer))
            serializer.is_valid(raise_exception=True)
            serializer.validated_data
            serializer.save()

        search_results(data_title, data_num)
        time.sleep(5)
        return Response(serializer.data)

class ValueSearchListView(generics.ListAPIView):
    queryset = ValueSearch.objects.all()
    print(queryset)
    serializer_class = ValueSearchSerializers