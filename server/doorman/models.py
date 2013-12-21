from django.db import models
from django.contrib.auth.models import User, UserManager

from django.db.models.signals import post_save
from django.dispatch import receiver


class RFIDTag(models.Model):
	tag     = models.CharField(max_length=200)
	user    = models.ForeignKey(User)

	def __unicode__(self):
		return (self.user.username+"_"+self.tag).strip().replace(" ", "")



class CheckIn(models.Model):
	time     = models.DateTimeField(auto_now=False, auto_now_add=True)
	user     = models.ForeignKey(User)

	def __unicode__(self):
		return self.user.username+'@'+self.time.strftime('%x_%X')


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	recentCheckin = models.ForeignKey(CheckIn, null=True)
	isPresent = models.BooleanField(default=True)
	RFIDTag = models.ForeignKey(RFIDTag, null=True)

	def __unicode__(self):
		return self.user.username+'_profile'

	def togglePresent(self):
		self.isPresent = not self.isPresent



# post_save handler for users
# @receiver(post_save, sender=User)
# def makeIsPresent(sender, created, instance, **kwargs):
# 	if(created):
# 		ip = isPresent(isPresent=True, user=instance)
# 		ip.save()
# 		print('created new boolean for user ' + instance.username)

@receiver(post_save, sender=CheckIn)
def toggle(sender, created, instance, **kwargs):
	if created:
		profile = instance.user.get_profile()
		profile.isPresent = not profile.isPresent
		profile.recentCheckin = instance
		profile.save()

		

@receiver(post_save, sender=User)
def makeProfile(sender, created, instance, **kwargs):
	if created:
		profile = UserProfile(user=instance)
		profile.save()
