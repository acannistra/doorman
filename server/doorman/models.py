from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
	

class RFIDTag(models.Model):
	tag     = models.CharField(max_length=200)
	user    = models.ForeignKey(User)

	def __unicode__(self):
		return (self.user.username+"_"+self.tag).strip().replace(" ", "")

class isPresent(models.Model):
	isPresent = models.BooleanField(default=False)
	user      = models.OneToOneField(User)

	def __unicode__(self):
		return(self.user.username+"_isPresent")

	def toggle(self):
		self.isPresent = not self.isPresent

class CheckIn(models.Model):
	time     = models.DateTimeField(auto_now=False, auto_now_add=True)
	user     = models.ForeignKey(User)

	def __unicode__(self):
		return self.user.username+'@'+self.time.strftime('%x_%X')

# post_save handler for users
@receiver(post_save, sender=User)
def makeIsPresent(sender, created, instance, **kwargs):
	if(created):
		ip = isPresent(isPresent=False, user=instance)
		ip.save()
		print('created new boolean for user ' + instance.username)

@receiver(post_save, sender=CheckIn)
def switchIsPresent(sender, created, instance, **kwargs):
	if created:
		user = instance.user
		user_ip = isPresent.objects.get(user=user)
		user_ip.toggle();
		user_ip.save()
