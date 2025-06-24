from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from .serializers import FeedSerializer
from rest_framework.exceptions import NotFound
# Create your views here.

class Feeds(APIView):
    #전체 게시글 조회
    def get(self, request):
        feeds = Feed.objects.all() #객체
        #객제 -> JSON(시리얼 라이즈)
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)

    def post(self, request):
        #역직렬화 (클라이언트가 보내준 json을 -> 객체로 변환)
        serializer = FeedSerializer(data=request.data)
        #유효성 검사
        if serializer.is_valid():
            serializer.save(user=request.user)
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound

    def get(self, request, feed_id):

        feed = self.get_object(feed_id)

        # feed (object) -> JSON(시리얼라이즈) 직렬화
        serializer = FeedSerializer(feed)
        # print(serializer.data)
        return Response(serializer.data)

