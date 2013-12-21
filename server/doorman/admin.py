from django.contrib import admin
from doorman.models import RFIDTag, isPresent, CheckIn

admin.site.register(RFIDTag)
admin.site.register(isPresent)
admin.site.register(CheckIn)
# Register your models here.
