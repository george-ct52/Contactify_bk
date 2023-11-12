from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name