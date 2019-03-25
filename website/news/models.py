from django.db import models


# Create your models here.
class Post(models.Model):
    Name = models.CharField(max_length=120)
    Topic = models.CharField(max_length=20)
    Post = models.TextField()
    Date = models.DateTimeField()

    def __str__(self):
        return self.Name

