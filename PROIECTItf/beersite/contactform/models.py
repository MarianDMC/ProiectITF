from django.db import models


# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.email
