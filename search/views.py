from rest_framework.response import Response
from rest_framework import status ,generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import *
from .serializers import *
import time
from googlesearch import search
class SearchBoxAPIView(APIView):
    def get(self, request):
        try:
            search_box = SearchBox.objects.all()
            serializer = SearchBoxSerializers(search_box, many=True)
            return Response(serializer.data)
        except SearchBox.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = SearchBoxSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        # #search to google
        # data_post = serializer.data
        # data_title = data_post['search_box']
        # data_num = data_post['number']
        # def search_results(query, number, advanced=True):
        #     titles = []
        #     urls = []
        #     for title in search(query, num_results=number, advanced=advanced):
        #         titles.append(title.title)
        #         urls.append(title.url)
        #     data = {'titles': titles, 'urls': urls}
        # search_results(data_title, data_num)
        # time.sleep(10)
        return Response(serializer.data)

class SearchAPIView(APIView):
    def get(self, request):
        data_search = SearchBox.objects.all().values()
        data_end = data_search[::-1][0]
        data_title = data_end['search_box']
        data_num = data_end['number']
        def search_results(query, number, advanced=True):
            titles = []
            urls = []
            for title in search(query, num_results=number, advanced=advanced):
                titles.append(title.title)
                urls.append(title.url)
            context = {'titles': titles, 'urls': urls}
            try:
                search_show = Search.objects.create(**context)
                serializer = SearchSerializers(search_show, many=True)
                return Response(serializer.data)
            except Search.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        search_results(data_title, data_num)
        time.sleep(7)


