from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponse, Http404
from doorman.models import CheckIn, User
from datetime import datetime

def index(request):
	times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return render(request, "index.html", {"time":times})
def userinfo(request, user_id):
	return HttpResponse("coming")





# Create your views here.
