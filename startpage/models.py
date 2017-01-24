from django.db import models
from django.utils import timezone

from geography.models import ZipCode

import os


#allow user to upload img
def get_image_ath(instance, filename):
   return os.path.join('photos', str(instance.id), filename)

class Musician(models.Model):

   user_name = models.CharField(max_length=30, primary_key=True)
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   current_rating = models.IntegerField()
   rating_text = models.TextField()
   bio = models.TextField()
   zip_code = models.ForeignKey(ZipCode)
   website = models.URLField()
   #profile pic
   #video mp4


class CreateProfile(models.Model):

   def create_profile(self, name_submitted):
      user_name = self.create(name_submitted=name_submitted)

      user_name = models.ForeignKey(User, unique=True)
      profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)

      return user_name

   def update_profile(self):
      return self



