from django.db import models

from geography.models import ZipCode

class Musician(models.Model):

   user_name = models.CharField(max_length=30, primary_key=True)
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   user_name = models.CharField(max_length=30, primary_key=True)
   current_rating = models.IntegerField()
   rating_text = models.TextField()
   zip_code = models.ForeignKey(ZipCode)
   #profile pic
   #video mp4

