from django.contrib import admin

# Register your models here.
from playspots_app import models

admin.site.register(models.Venue)
admin.site.register(models.User)