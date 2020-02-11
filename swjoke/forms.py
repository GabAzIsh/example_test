from django import forms
from django.forms import ModelForm, RadioSelect, formset_factory
from django.shortcuts import get_object_or_404,redirect, render


from .models import Recruit, SithPlanets, Test, Question, Answer

class RecruitForm(forms.ModelForm):
    
    # recruit_planet = forms.ModelChoiceField(queryset=SithPlanets.objects.all(), widget=forms.Select(attrs={'class':'hidden'}))
    class Meta:
        model = Recruit
        fields = ['recruit_name','recruit_age', 'recruit_email', 'recruit_planet']

        #Recruit_widget_class_attribute = {'class': 'form-control'}

        widgets = {
            'recruit_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recruit_age': forms.TextInput(attrs={'class': 'form-control', 'min': 1,'max': 300,'type': 'number'}),
            'recruit_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'recruit_planet': forms.Select(attrs={'class': 'form-control'}),
        }

    
    
    # recruit_name = forms.CharField(max_length=100)
    # recruit_age = forms.IntegerField(max_value=900, min_value=1)
    # recruit_email = forms.EmailField(max_length=100)
    # recruit_planet = forms.ModelChoiceField(queryset=SithPlanets.objects.all())

    # recruit_name.widget.attrs.update({'class': 'form-control'})
    # recruit_age.widget.attrs.update({'class': 'form-control'})
    # recruit_email.widget.attrs.update({'class': 'form-control'})
    # recruit_planet.widget.attrs.update({'class': 'form-control'})

    # def save(self,request):
    #     new_recruit = Recruit.objects.create(
    #         recruit_name = self.cleaned_data['recruit_name'],
    #         recruit_age = self.cleaned_data['recruit_age'],
    #         recruit_email = self.cleaned_data['recruit_email'],
    #         recruit_planet = self.cleaned_data['recruit_planet']
    #     )
    #     return render(request, 'swjoke/shadow_hand_test.html', context={'recruit_name' : self.cleaned_data['recruit_name'] })

class SimpleRecruitForm(ModelForm):

    class Meta:
        model = Test

        exclude = ['questions']
        #fields = '__all__'#['question_text', '']

    duration = forms.CharField(widget = forms.TextInput(attrs =   
                        {'min': 20,'max': 300,'type': 'number'}))    
    questions = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Question.objects.all()
               )

class AnswerForm(ModelForm):
    
    def __init__ (self, *args, **kwargs):
        # print(self)
        print(kwargs)
        self.title = kwargs['initial']['title']
        super ().__init__ (*args, **kwargs) # call base class


    def save(self, request, question_id, recruit_id):
        new_answer = Answer.objects.create(
            question = Question.objects.get(pk=question_id),
            recruit = Recruit.objects.get(pk=recruit_id) ,
            answer = self.cleaned_data['answer']
        )
        return render(request, 'swjoke/index.html')


    class Meta:
        model = Answer

        fields = ['answer']
        widgets = {
            'answer': RadioSelect
        }
        labels = {
            "answer": ''
        }



AnswerFormSet=formset_factory(AnswerForm,extra=0)


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=100)

Simpleformset=formset_factory(SimpleForm, extra=1)