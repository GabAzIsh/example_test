from django import forms
from django.forms import ModelForm, RadioSelect, HiddenInput, formset_factory
from django.shortcuts import get_object_or_404,redirect, render


from .models import Recruit, SithPlanets, Test, Question, Answer

class RecruitForm(forms.ModelForm):
   
    class Meta:
        model = Recruit
        fields = ['recruit_name','recruit_age', 'recruit_email', 'recruit_planet']

        widgets = {
            'recruit_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recruit_age': forms.TextInput(attrs={'class': 'form-control', 'min': 1,'max': 300,'type': 'number'}),
            'recruit_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'recruit_planet': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_recruit_email(self):
        recruit_email = self.cleaned_data['recruit_email'].lower()
        if Recruit.objects.filter(recruit_email__iexact=recruit_email).exists():
            raise forms.ValidationError(f'{recruit_email} already exist. Email addresses must be unique.')
        return recruit_email







class AnswerForm(ModelForm):
    
    def __init__ (self, *args, **kwargs):
        try:
            self.title = kwargs['initial']['title']
        except:
            self.title = ''
        super ().__init__ (*args, **kwargs) 

    class Meta:
        model = Answer

        fields = ['answer', 'question', 'recruit']
        widgets = {
            'answer': RadioSelect,
            'question': HiddenInput,
            'recruit': HiddenInput
        }
        labels = {
            "answer": ''
        }



AnswerFormSet=formset_factory(AnswerForm,extra=0)