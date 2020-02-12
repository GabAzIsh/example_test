import uuid
from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.question_text)


class SithPlanets(models.Model):
    planet_name = models.CharField(max_length=40, unique = True)

    def __str__(self):
        return self.planet_name

class Test(models.Model):
    questions = models.ManyToManyField(Question, blank=True) 
    planet = models.OneToOneField(SithPlanets, on_delete=models.CASCADE, related_name='test', blank=True, null=True)
    unique_sith_order_code = models.UUIDField(
        default = uuid.uuid4, 
        editable = False
    )

    def __str__(self):
        return str('Test ' + str(self.pk) + ' UUID:' + str(self.unique_sith_order_code))





class Sith(models.Model):

    sith_name = models.CharField(max_length=100)
    sith_planet = models.ForeignKey(SithPlanets, on_delete=models.CASCADE)

    def __str__(self):
        return self.sith_name

    def get_absolute_url(self):
        return reverse('swjoke:detail', kwargs={'pk': self.pk})

class Recruit(models.Model):

    recruit_planet = models.ForeignKey(SithPlanets, on_delete=models.CASCADE)
    recruit_name = models.CharField(max_length=100)
    recruit_age = models.PositiveIntegerField()
    recruit_email = models.EmailField(max_length=100)
    shadow_hand = models.ForeignKey(Sith,  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.recruit_name

    def get_absolute_url(self):
        return reverse('swjoke:detail', kwargs={'pk': self.pk})



class Answer(models.Model):
    answer = models.CharField(max_length=3, choices=[
    ('yes', 'yes'),
    ('no', 'no')], default='no')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)

    def __str__(self):
        return self.recruit.recruit_name + '_' + self.question.question_text



    
