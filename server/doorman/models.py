from django.db import models

class User(models.Model):
	name 	 = models.CharField(max_length=200)
	rfid     = models.CharField(max_length=200, primary_key=True)
	has_rfid = models.BooleanField(default=False)
	image 	 = models.URLField()
	email    = models.EmailField()


class CheckIn(models.Model):
	time     = models.DateTimeField(auto_now=False, auto_now_add=True)
	user     = models.ForeignKey(User)

