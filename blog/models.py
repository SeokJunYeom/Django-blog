from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to = "blog/static/gochiusa")
    name = models.CharField(max_length = "20")
    birth = models.CharField(max_length = "20")
    stature = models.CharField(max_length = "20")
    blood_type = models.CharField(max_length = "20")

    def __str__(self):
        return self.name
