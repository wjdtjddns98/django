from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=5)

