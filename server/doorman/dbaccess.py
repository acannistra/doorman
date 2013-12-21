# dbaccess.py
from doorman.models import CheckIn, User


def mostRecentCheckin(user):
	try:
		return CheckIn.objects.filter(user=user).latest('time')
	except:
		return 0
