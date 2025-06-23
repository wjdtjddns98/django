from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)  # 사용자 정보 직렬화
    class Meta:
        model = Feed
        fields = "__all__" #모든 필드를 직렬화 한다는 뜻
        depth = 1