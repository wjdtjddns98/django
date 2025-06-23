from django.db import models

from common.models import CommonModel


# Create your models here.
class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300)

    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

