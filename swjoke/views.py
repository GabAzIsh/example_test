from django.shortcuts import get_object_or_404,redirect, render
from django.views import generic, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.
from .models import Recruit, Sith, SithPlanets, Test, Question
from .forms import RecruitForm, SimpleRecruitForm, AnswerFormSet, Simpleformset


class IndexView(TemplateView):
    template_name = 'swjoke/index.html'
    # return render(request, 'swjoke/index.html')
    # base_url = reverse('swjoke:black')
    # query_string =  urlencode({'chrom': 'What the hell MF?'})
    # url = f'{base_url}?{query_string}'
    # return redirect(url)

class Romb(View):

    def dispatch(self, request, *args, **kwargs):
        
        if request.method == 'GET':
            id = int(request.GET.get('recruit_id'))
        elif request.method == 'POST':
            id = int(request.POST.get('recruit_id'))

        self.recruit = Recruit.objects.get(pk=id)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        #print(request)
        print('1')
        r=self.recruit
        print(r)
        try:
            test = q.recruit_planet.test
        except:
            test = Test.objects.get(pk=1) 
        d = [ {'question': question, 'recruit': r, 'title': question.question_text} for question in test.questions.all()]
        print(d)
        # for index, question in enumerate(test.questions.all(),1):
        #     print(index, question)
        # q1=Question.objects.get(pk=1)
        # q2=Question.objects.get(pk=2)
        # q3=Question.objects.get(pk=3)
        # d1={'question': q1, 'recruit': r, 'title': q1.question_text}
        # d2={'question': q2, 'recruit': r, 'title': q2.question_text}
        # d3={'question': q3, 'recruit': r, 'title': q3.question_text}
        
        formset = AnswerFormSet( initial=d)
        # print(dir(AnswerFormSet))
        # print(formset)
        return render(request, 'swjoke/black_test.html', context={'formset' : formset})
    # name=self.args[chrom]
    # print(self.chrom)
    #    return render(request, 'swjoke/index.html')

    def post(self, request):

        r=Recruit.objects.get(pk=1)
        q1=Question.objects.get(pk=1)
        q2=Question.objects.get(pk=2)
        q3=Question.objects.get(pk=3)
        d1={ 'title': ''}
        d2={'title': ''}
        d3={'title': ''}
        initial=[d1, d2, d3]
        print(request.__dict__)
        print('Post')
        print('No')
        formset = AnswerFormSet(request.POST, initial=[d1, d2, d3])
        print('formset is Yes')
        # print(formset)
        print('HA-ha')
        print(request.POST)
        if formset.is_valid():#, request.FILES
            print('FormSet is Valid')
        else:
            print('Formset IS NOT valid')
        print('No, I can\'t see this')
        # for form in formset:
        #     print(form)
        #     print('tur HA-HA tur HA-HA')
        # if formset.is_valid():
        #     print('Valid')
        #     t = Recruit.objects.all()
        #     for form in formset:
        #         p = form.cleaned_data.get('players')
        #         scoreSave = form.save(commit=False)
        #         scoreSave.turn = t
        #         scoreSave.save()
        #         scoreSave.players.add(p)
        # else:
        #     print('Formset not OK')
        #     return render(request, 'scorer/game.html',
        #           {})



# class IndexView(generic.ListView):
#     template_name = 'swjoke/test.html'
#     context_object_name = 'question_list'

#     def get_queryset(self):
#         """
#         Return random five  questions.
#         """
#         return Question.objects.order_by('?')[:3]

class RecruitDetailView(generic.DetailView):
    model = Recruit
    template_name = 'swjoke/detail.html'
    context_object_name = 'object'

class RecruitCreateView(generic.FormView):
    template_name = 'swjoke/contact.html'
    form_class = SimpleRecruitForm
    success_url = '/swjoke/'

class SithDetailView(generic.DetailView):
    model = Sith
    template_name = 'swjoke/detail.html'
    context_object_name = 'object'

class RecruitCreate(View):
   
   
    def get(self, request):
        form = RecruitForm()
        return render(request, 'swjoke/new_recruit.html', context={'form' : form})
    
    
    def post(self, request):
        bound_form = RecruitForm(request.POST)
        print(request.POST)
        if bound_form.is_valid():
            new_recruit = bound_form.save()
            print(new_recruit.__dict__)
            base_url = reverse('swjoke:black_test')
            query_string =  urlencode({'recruit_id': new_recruit.pk })
            url = f'{base_url}?{query_string}'
            return redirect(url)
            # return render(request, 'swjoke/black_test.html', context={'recruit_id' : new_recruit.pk })
        else:
            print('Yoho-ho')
            return render(request, 'swjoke/new_recruit.html', context={'form' : bound_form})
        print('Yoho-ho2')

class ShadowHand(View):

    
    def get(self, request):
        formset = Simpleformset()
        print(formset)
        return render(request, 'swjoke/shadow_hand_test.html', context={'formset' : formset})

    def post(self, request):
        formset=Simpleformset(request.POST)
        print(request.__dict__)
        print(formset.__dict__)
        for form in formset:
            print(form)
        print(formset.is_valid())
        print('Good')
        # if formset.is_valid():
        #     print('Yes')