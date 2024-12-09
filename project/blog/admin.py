from django.contrib import admin
from .models import *

admin.site.register(Myblog),
admin.site.register(Item),
admin.site.register(Person)