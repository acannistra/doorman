from django.contrib import admin
from doorman.models import RFIDTag, isPresent

admin.site.register(RFIDTag)
admin.site.register(isPresent)
# Register your models here.
