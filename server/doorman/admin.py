from django.contrib import admin
from doorman.models import RFIDTag, CheckIn, UserProfile

admin.site.register(RFIDTag)
admin.site.register(UserProfile)
admin.site.register(CheckIn)
# Register your models here.
