from django.db import models

#게시글
#title, content, author, created_at, updated_at
class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()



