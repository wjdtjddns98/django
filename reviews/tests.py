from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Review
from users.models import CustomUser
from feeds.models import Feed

class ReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password")
        refresh = RefreshToken.for_user(self.user)
        self.token = refresh.access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        #Feed Model
        self.feed = Feed.objects.create(user=self.user, title="New title")

        #review Model

        self.review1 = Review.objects.create(content="content1", user=self.user, feed=self.feed)
        self.review2 = Review.objects.create(content="content2", user=self.user, feed=self.feed)

    def test_get_all_reviews(self):
        url = reverse("reviews")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), 2)


    def test_get_review_detail(self):
        url = reverse("review_detail", kwargs={"review_id": 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["content"], self.review1.content)





# Create your tests here.
