from django.shortcuts import render
from rest_framework.views import APIView
from .models import Review
from .serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404







class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)

# Create your views here.

class ReviewDetail(APIView):
    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)

        serializer = ReviewSerializer(review)
        return Response(serializer.data)
