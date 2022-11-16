from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .models import ValueSearch, SearchBox
from .serializers import ValueSearchSerializers, SearchBoxSerializers
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
        # get data title request
        title_data_request = serializer.data['title']
        #search to google
        data_search = SearchBox.objects.all().values()
        last_data = data_search[::-1][0]
        data_title = last_data['title']
        data_num = last_data['number']
        def search_results(query, number, advanced=True):
            titles = []
            urls = []
            result = {'title': title_data_request}
            for title in search(query, num_results=number, advanced=advanced):
                titles.append(title.title)
                urls.append(title.url)
            # sava data one to one
            for num in range(len(titles)):
                result['titles'] = titles[num]
                result['urls'] = urls[num]
                #desrializers data
                serializer = ValueSearchSerializers(data=result)
                serializer.is_valid(raise_exception=True)
                serializer.validated_data
                serializer.save()
        search_results(data_title, data_num)
        time.sleep(5)
        return Response(serializer.data)
@api_view()
def ValueSearching(request):
    if request.method == "GET":
        data_search = SearchBox.objects.all().values()
        last_data = data_search[::-1][0]
        data_title = last_data['title']
        queryset = ValueSearch.objects.filter(title=data_title)
        serializer_class = ValueSearchSerializers(queryset, many=True)
        return Response(serializer_class.data)






