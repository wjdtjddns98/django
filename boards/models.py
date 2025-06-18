from django.db import models
from common.models import CommonModel


#게시글
#title, content, author, created_at, updated_at
class Board(CommonModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
