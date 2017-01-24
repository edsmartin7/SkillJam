from django.shortcuts import render
from django.htttp import HttpResponse

from startpage.models import Musician
from startpage.models import CreateProfile

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

def user_profile(request, user_id):
   #profile = Musician.objects.get(pk=user_id) #request.get()
   #template = loader.get_tempate('startpage/index.html')
   #context = { 'profile': profile }
   #return HttpResponse(template.render(context, request)

   #request.get()
   #data = self.model.objects.using('dbname')

   return HttpResponse("This is %s Profile Page " % user_id)

def all_profile(request):
   #sort by rating, closest zip, instrument
   return HttpResponse("All profiles sorted by closest zip")
   



