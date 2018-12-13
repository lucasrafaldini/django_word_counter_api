from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CountSerializer, CountSerializer2
from .counter import processing
import requests


class CountView(APIView):

    def get(self, request):
        if request.query_params.get('url2'):
            word = request.query_params.get('word')
            url1 = request.query_params.get('url1')
            url2 = request.query_params.get('url2')
            serializer = CountSerializer2(data={"word": word, "url1": url1, "url2":url2})
            if cache.get(word+url1+url2):
                cache_url = cache.get(word+url1+url2)
		cache_url = cache_url
                return Response({word: cache_url}, status=status.HTTP_200_OK)
            else:
                if not serializer.is_valid():
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)
                try:
                    # Headers to prevent encoding errors
                    headers = {'Accept-Encoding': 'identity'}
                    response1 = requests.get(url1, headers=headers)
                    response2 = requests.get(url2, headers=headers)
                except:
                    return Response({"url": ["Page unavailable"]}, status=status.HTTP_400_BAD_REQUEST)

                occurrences = processing.counter2(self, word=word, text1=response1.text, text2=response2.text)

               #definindo low-level cache com timeout de meia hora
                cache.set((word+url1+url2),{url1: occurrences[0], url2: occurrences[1]},timeout=1800)
                return Response({word: {url1: occurrences[0], url2: occurrences[1]}}, status=status.HTTP_200_OK)

        else:
            word = request.query_params.get('word')
            url = request.query_params.get('url')
            serializer = CountSerializer(data={"word": word, "url": url})
            if cache.get(word+url):
                cache_url = cache.get(word+url)
		cache_url = cache_url
                return Response({word: cache_url}, status=status.HTTP_200_OK)
            else:
                if not serializer.is_valid():
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)

                try:
                    # Headers to prevent encoding errors
                    headers = {'Accept-Encoding': 'identity'}
                    response = requests.get(url, headers=headers)
                except:
                    return Response({"url": "Page unavailable"}, status=status.HTTP_400_BAD_REQUEST)

                occurrence = processing.counter1(self, word=word, text=response.text)

                # definindo low-level cache com timeout de meia hora
                cache.set(str(word+url), {occurrence}, timeout=1800)
                return Response({word: occurrence}, status=status.HTTP_200_OK)