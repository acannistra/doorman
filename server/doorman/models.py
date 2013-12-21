from django.db import models

class User(models.Model):
	name 	 = models.CharField(max_length=200)
	rfid     = models.CharField(max_length=200, primary_key=True)
	image 	 = models.URLField(null=True)
	email    = models.EmailField()
	handle	 = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.name;


class CheckIn(models.Model):
	time     = models.DateTimeField(auto_now=False, auto_now_add=True)
	user     = models.ForeignKey(User)
