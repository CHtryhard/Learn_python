from django.db import models

# Create your models here.
class UsersRecord(models.Model):
    name = models.CharField(max_length = 264)
    email = models.EmailField(max_length = 264, unique = True)
