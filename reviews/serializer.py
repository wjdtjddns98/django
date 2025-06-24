from rest_framework.serializers import ModelSerializer
from reviews.models import Review
from users.serializers import FeedUserSerializer


class ReviewSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)  # 사용자 정보 직렬화
    class Meta:
        model = Review
        fields = "__all__"
