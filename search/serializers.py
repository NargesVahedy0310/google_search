from rest_framework import serializers
from .models import *
from .googel_search import *

class SearchSerializers(serializers.Serializer):
    class Meta:
        model = Search
        fields = ('id', 'titles', 'urls')



class SearchBoxSerializers(serializers.Serializer):
    search_box = serializers.CharField(max_length=300)
    number = serializers.IntegerField()
    def create(self, validated_data):
        return SearchBox.objects.create(**validated_data)
    class Meta:
        model = SearchBox
        fields = ('id', 'search_box', 'number')