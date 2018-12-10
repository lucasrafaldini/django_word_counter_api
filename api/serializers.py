from rest_framework import serializers


class CountSerializer(serializers.Serializer):
    url = serializers.URLField()
    word = serializers.CharField(max_length=100)

class CountSerializer2(serializers.Serializer):
    url1 = serializers.URLField()
    url2 = serializers.URLField()
    word = serializers.CharField(max_length=100)