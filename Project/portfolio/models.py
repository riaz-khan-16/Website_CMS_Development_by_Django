from django.db import models

# Create your models here.


class Page1(models.Model):
        fname = models.CharField(max_length=255)
        lname = models.CharField(max_length=255)
        prof = models.CharField(max_length=255)
        logo = models.CharField(max_length=255,null=True)

class About(models.Model):
        fname = models.CharField(max_length=255)
        lname = models.CharField(max_length=255)
        prof = models.CharField(max_length=255)
        about = models.CharField(max_length=255)
        ffrom = models.CharField(max_length=255)
        live = models.CharField(max_length=255)
        age = models.CharField(max_length=255)
        gender = models.CharField(max_length=255)

          
