from rest_framework import serializers
from .googel_search import *

class SearchSerializers(serializers.Serializer):
    # titles = serializers.CharField(max_length=255)
    # urls = serializers.CharField(max_length=255)
    class Meta:
        model = Search
        fields = ('id', 'titles', 'urls')



class SearchBoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = SearchBox
        fields = ('id', 'search_box', 'number')

