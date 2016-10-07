from django.db import models
from django.conf import settings

# Create your models here.


class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to = "gochiusa")
    name = models.CharField(max_length = 20)
    birth = models.CharField(max_length = 20)
    stature = models.CharField(max_length = 20)
    blood_type = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
