from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "is_superuser")
        # fields = "__all__"

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"