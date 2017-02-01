from django.shortcuts import render
from django.http import HttpResponse

from startpage.models import Musician
from startpage.models import CreateProfile

import logging

logger = logging.getLogger(__name__)


def user_profile(request):
#def user_profile(request, user_id):
   #profile = Musician.objects.get(pk=user_id) #request.get()
   #template = loader.get_tempate('startpage/index.html')
   #context = { 'profile': profile }
   #return HttpResponse(template.render(context, request)

   #request.get()
   #data = self.model.objects.using('dbname')

   return render(request, 'startpage/index.html')

def all_profile(request):
   #sort by rating, closest zip, instrument
   return HttpResponse("All profiles sorted by closest zip")
   
def login_page(request):
   #user_id = 
   #user_pass = 
   return render(request, 'startpage/login.html')

def game_mode(request):
   return HttpResponse("You are now in Game Mode")


