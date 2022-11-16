from rest_framework import serializers
from .models import *

class SearchBoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = SearchBox
        fields = ('title', 'number')

class ValueSearchSerializers(serializers.ModelSerializer):

    class Meta:
        model = ValueSearch
        fields = ('title', 'titles', 'urls')

        def create(self, validated_data):
            return ValueSearch.objects.create(**validated_data)

