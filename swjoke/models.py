import uuid
from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Test(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=3, choices=[
        ('yes', 'yes'),
        ('no', 'no')], default='no')
    unique_sith_order_code = models.UUIDField(
        default = uuid.uuid4, 
        editable = False
    )

    def __str__(self):
        return str(self.unique_sith_order_code)

class SithPlanets(models.Model):
    planet_name = models.CharField(max_length=40, unique = True)

    def __str__(self):
        return self.planet_name




class Recruit(models.Model):

    recruit_planet = models.ForeignKey(SithPlanets, on_delete=models.CASCADE)
    recruit_name = models.CharField(max_length=100)
    recruit_age = models.PositiveIntegerField()
    recruit_email = models.EmailField(max_length=100)
    recruit_questions = models.ManyToManyField(Test) 

    def __str__(self):
        return self.recruit_name

    def get_absolute_url(self):
        return reverse('swjoke:detail', kwargs={'pk': self.pk})


class Sith(models.Model):

    sith_name = models.CharField(max_length=100)
    sith_planet = models.ForeignKey(SithPlanets, on_delete=models.CASCADE)

    def __str__(self):
        return self.sith_name

    def get_absolute_url(self):
        return reverse('swjoke:detail', kwargs={'pk': self.pk})



#class TestChoices(models.Model):


    
