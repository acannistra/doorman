from django.db import models
from django.contrib.auth.models import User, UserManager

from django.db.models.signals import post_save
from django.dispatch import receiver

'''
	RFIDTag is a representation of an RFID device. Each RFID Tag is
	associated with a single user.
'''
class RFIDTag(models.Model):
	tag     = models.CharField(max_length=200)
	user    = models.ForeignKey(User)

	def __unicode__(self):
		return (self.user.username+"_"+self.tag).strip().replace(" ", "")

'''
	A CheckIn represents a single actuation of the RFID reader. A timestamp
	(currently server-recorded, 12/21/13) and a user is associated. 

	TODO: Do we want to keep all checkins? 
'''
class CheckIn(models.Model):
	time     = models.DateTimeField(auto_now=False, auto_now_add=True)
	user     = models.ForeignKey(User)
	tag      = models.ForeignKey(RFIDTag)

	def __unicode__(self):
		return self.user.username+'@'+self.time.strftime('%x_%X')

'''
	** Note. This is *NOT* how user data should be handled in Django. 
	If I wasn't pressed for time this would certainly be encompassed in a 
	subclass of django.contrib.auth.models.User.

	UserProfile adds additional data to each user. It holds onto the most recentCheckin, 
	whether or not the user is home, and their RFIDTags

	TODO: Figure out if that RFID tag parameter is necessary even a little.

'''
class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	recentCheckin = models.ForeignKey(CheckIn, null=True)
	isPresent = models.BooleanField(default=True)
	RFIDTag = models.ForeignKey(RFIDTag, null=True)

	def __unicode__(self):
		return self.user.username+'_profile'

	def togglePresent(self):
		self.isPresent = not self.isPresent

# Here are Django Signal handlers, actuated when instances of the above models
# are created. 

'''
	Actuated on creation of a *new* checkin. 
	* Toggles user's "is present" parameter in User Profile
	* Adds itself to most recent checkin parameter in corresponding user profile
'''
@receiver(post_save, sender=CheckIn)
def toggle(sender, created, instance, **kwargs):
	if created:
		profile = instance.user.get_profile()
		profile.isPresent = not profile.isPresent
		profile.recentCheckin = instance
		profile.save()

		
'''
	Creates a new user profile to correspond with the creation of 
	each new user by Django's auth modules. 
'''
@receiver(post_save, sender=User)
def makeProfile(sender, created, instance, **kwargs):
	if created:
		profile = UserProfile(user=instance)
		profile.save()
