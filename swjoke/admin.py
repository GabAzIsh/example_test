from django.contrib import admin
from .models import Recruit, Sith, SithPlanets, Test

# Register your models here.
admin.site.register(Recruit)
admin.site.register(Sith)
admin.site.register(Test)
admin.site.register(SithPlanets)