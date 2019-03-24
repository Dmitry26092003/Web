from django.db import models


# Create your models here.
class Files(models.Model):
    Name = models.CharField(max_length=120)
    Description = models.TextField()
    Date = models.DateTimeField()
    Genre = models.CharField(max_length=20)
    FileName = models.CharField(max_length=120)

    def __str__(self):
        return self.Name

