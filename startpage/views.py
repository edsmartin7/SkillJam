from django.shortcuts import render
from startpage.models import Musician

import logging

logger = logging.getLogger(__name__)

class StartPageHandler():
   methods = ('GET', 'POST', 'PUT', 'DELETE')
   fields = 
   exclude = 
   model = 

   #GET
   def read(self, request):
      current = Reporter()
      #current = self.get_dict(request.GET)
      current.save()
      Musician.objects.all()
      musician = Musician.objects.get(id=self)
      return render(request, 'startpage/user_profile.html', {'musician': musician})

   #POST
   def create(self, request):

   #PUT
   def update(self, request):

   #DESTROY
   def delete(self, request):



