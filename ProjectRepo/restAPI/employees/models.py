from django.db import models

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length=10)
    Secondname = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname
