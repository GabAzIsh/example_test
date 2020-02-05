from django import forms
from .models import Recruit, SithPlanets

class RecruitForm(forms.Form):
    recruit_name = forms.CharField(max_length=100)
    recruit_age = forms.IntegerField()
    recruit_email = forms.EmailField(max_length=100)
    recruit_planet = forms.ModelChoiceField(queryset=SithPlanets.objects.all())

    recruit_name.widget.attrs.update({'class': 'form-control'})
    recruit_age.widget.attrs.update({'class': 'form-control'})
    recruit_email.widget.attrs.update({'class': 'form-control'})
    recruit_planet.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_recruit = Recruit.objects.create(
            recruit_name = self.cleaned_data['recruit_name'],
            recruit_age = self.cleaned_data['recruit_age'],
            recruit_email = self.cleaned_data['recruit_email'],
            recruit_planet = self.cleaned_data['recruit_planet']
        )
        return new_recruit

