from django.db import models
from django.contrib.auth.models import User



class RFIDTag(models.Model):
	tag     = models.CharField(max_length=200)
	user    = models.ForeignKey(User)

	def __unicode__(self):
		return (self.user.username+"_"+self.tag).strip().replace(" ", "")

class isPresent(models.Model):
	isPresent = models.BooleanField(default=False)
	user      = models.OneToOneField(User)

class CheckIn(models.Model):
	time     = models.DateTimeField(auto_now=False, auto_now_add=True)
	user     = models.ForeignKey(User)
