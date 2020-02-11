from django.contrib import admin
from django.db import models
from django import forms
from .models import Question, Recruit, Sith, SithPlanets, Test, Answer


class TestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }

# Register your models here.
admin.site.register(Recruit)
admin.site.register(Sith)
admin.site.register(Test, TestAdmin)
admin.site.register(SithPlanets)
admin.site.register(Question)
admin.site.register(Answer)

