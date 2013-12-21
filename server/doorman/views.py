from django.shortcuts import render, get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from doorman.models import CheckIn, User
from datetime import datetime
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc




@login_required
def index(request):
	times = datetime.now()
	usersPresent = User.objects.get(isPresent=true)
	return render(request, "index.html", {"time":times})

@login_required
def userinfo(request, user_id):
	user = get_object_or_404(User, username=user_id)

	return render(request, "user.html", {"user":user})

def logout_view(request):

	return HttpResponse('/accounts/login')


