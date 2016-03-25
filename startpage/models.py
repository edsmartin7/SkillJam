from django.db import models

from geography.models import ZipCode

class Musician(models.Model):
   rating_text = models.CharField(max_length=10)
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   user_name = models.CharField(max_length=30, primary_key=True)
   current_rating = models.IntegerField()
   zip_code = models.ForeignKey(ZipCode)
   #video mp4

   
