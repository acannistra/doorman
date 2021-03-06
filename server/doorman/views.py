from django.shortcuts import render, get_object_or_404, render, redirect
from django.http import HttpResponse, Http404

from doorman.models import CheckIn, User, RFIDTag, UserProfile

from datetime import datetime
from django.utils.timezone import utc

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers



'''
	Responsible for generating the data to send to the main page's 
	template, including the current list of users, and in the future 
	some aggregate statistics about the data and possibly 
	even the makings of some plots. 

	Login is required.
'''

@login_required
def mainpage_view(request):
	time = datetime.now()
	profiles = UserProfile.objects.all()
	users    = User.objects.all()
	checkins = CheckIn.objects.all()
	return render(request, "index.html", 
		{
			'users':serializers.serialize('json', profiles),
			'time':time,
		 	'profiles':profiles,
		 	'checkins':checkins
		})


'''
	Responsible for generating data about an individual user. 
	Must be sent a valid user_id which is the User.username field
'''
@login_required
def userinfo(request, user_id):
	user = get_object_or_404(User, username=user_id)

	return render(request, "user.html", {"user":user})

@login_required
def chart(request, type):
	# write this function
	pass

'''
	This is the critical method for sending checkins to the system.
	It takes a POST request only, with only 1 parameter, the RFID tag 
	identifier (POSTed as 'rfid')

	TODO: Make this less horribly insecure. Authentication would be nice. 
	We could start simple with just a key of some sort, but password Authentication
	would be most ideal.

'''

@csrf_exempt
def checkin_view(request):
	if request.method == 'POST':
		rfid = request.POST['rfid'];
		time = datetime.now();
		dbtag = get_object_or_404(RFIDTag, tag=rfid)
		checkin = CheckIn(time=time, user=dbtag.user, tag=dbtag)
		checkin.save()
		return HttpResponse('OK: ('+rfid+'->'+dbtag.user.username+')')

