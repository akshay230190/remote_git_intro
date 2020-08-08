from django.db import models
class Adduser(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.email}"


# Create your models here.
