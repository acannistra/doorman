from django.shortcuts import render, get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from doorman.models import CheckIn, User, RFIDTag, UserProfile
from datetime import datetime
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from django.views.decorators.csrf import csrf_exempt
from dbaccess import mostRecentCheckin



@login_required
def mainpage_view(request):
	time = datetime.now()
	profiles = UserProfile.objects.all()
	return render(request, "index.html", 
		{
			'time':time,
		 	'profiles':profiles
		})

@login_required
def userinfo(request, user_id):
	user = get_object_or_404(User, username=user_id)

	return render(request, "user.html", {"user":user})

def logout_view(request):

	return HttpResponse('/accounts/login')


@csrf_exempt
def checkin_view(request):
	if request.method == 'POST':
		rfid = request.POST['rfid'];
		time = datetime.now();
		dbtag = get_object_or_404(RFIDTag, tag=rfid)
		checkin = CheckIn(time=time, user=dbtag.user)
		checkin.save()
		return HttpResponse('OK: ('+rfid+'->'+dbtag.user.username+')')

