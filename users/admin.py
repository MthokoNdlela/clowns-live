from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Client)
admin.site.register(Clown)
admin.site.register(Tag)
admin.site.register(Order)