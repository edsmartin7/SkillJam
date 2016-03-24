from django.db import models

# Create your models here.

class Rating(models.Model):
   rating_text = models.CharField(max_length=10)


