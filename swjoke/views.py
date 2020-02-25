from django.shortcuts import get_object_or_404,redirect, render, HttpResponse
from django.views import generic, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail

from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.
from .models import Recruit, Sith, SithPlanets, Test, Question
from .forms import RecruitForm,  AnswerFormSet


class IndexView(TemplateView):
    template_name = 'swjoke/index.html'
    def dispatch(self, request, *args, **kwargs):
        try:
            Test.objects.get(pk=1)
        except:
            return render(request, 'swjoke/error.html')
        return super().dispatch(request, *args, **kwargs)




class SithList(generic.ListView):
    model = Sith
    template_name = 'swjoke/sith_list.html'
    context_object_name = 'sith_list'





class SithUpdateRedirect(generic.RedirectView):
    
    @staticmethod
    def record_shadow_hand(recruit_id, sith_id):
            sith_id =int(sith_id)
            recruit_id =int(recruit_id)
            recruit=Recruit.objects.get(id=recruit_id)
            sith=Sith.objects.get(id=sith_id)
            recruit.shadow_hand = sith
            recruit.save()
# Sending email by gmail
            recipients=[recruit.recruit_email]
            subject='From Unseriously Order of the Sith Django website'
            message=f'{recruit.recruit_name} You are become Shadow Hand of {sith.sith_name}'
            sender='captain.justy.ueki.taylor@gmail.com'  
            send_mail(subject, message, sender, recipients, fail_silently=False)

    def dispatch(self, request, *args, **kwargs):
        self.planet_id = kwargs['planet_sith_id']
        self.sith_id = kwargs['sith_id']
        if request.method == 'POST':
            self.recruit_id = request.POST.get("recruit_id")
            self.record_shadow_hand(self.recruit_id, self.sith_id)

        return super().dispatch(request, *args, **kwargs)

    pattern_name = 'swjoke:recruit_list'
    permanent = False
    query_string = True





class RecruitList(generic.ListView):

    def dispatch(self, request, *args, **kwargs): 
        self.planet_id = kwargs['planet_sith_id']
        self.sith_id = kwargs['sith_id']
        if len(Sith.objects.get(id = int(self.sith_id)).recruit_set.all()) >= 3:
            return render(request, 'swjoke/index.html', {'text': 'You have reached maximum number of Shadow Hand', 'color': 'alert alert-warning'})
        return super().dispatch(request, *args, **kwargs)

    model = Recruit
    template_name = 'swjoke/recruit_list.html'
    context_object_name = 'recruit_list'

    def get_queryset(self):
        """
        Return Sith with.
        """
        return Recruit.objects.filter(shadow_hand=None).filter(
            recruit_planet_id=self.planet_id
        ).order_by('-recruit_name')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['sith_id'] = self.sith_id
        context['planet_sith_id'] = self.planet_id
        return context





class BlackTest(View):

    def dispatch(self, request, *args, **kwargs):        
        if request.method == 'GET':
            id = int(request.GET.get('recruit_id'))
            self.recruit = Recruit.objects.get(pk=id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        r=self.recruit
        try:
            test = q.recruit_planet.test
        except:
            test = Test.objects.get(pk=1) 
        d = [ {'question': question, 'recruit': r, 'title': question.question_text} for question in test.questions.all()]
        formset = AnswerFormSet( initial=d)
        return render(request, 'swjoke/black_test.html', context={'formset' : formset})

    def post(self, request):
        formset=AnswerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return render(request, 'swjoke/index.html', {'text': 'You personal information was sucsefully registrated. Sith decision will be sended to you later', 'color': 'alert alert-success'})
        return render(request, 'swjoke/black_test.html', context={'formset' : formset})






class RecruitDetailView(generic.DetailView):
    model = Recruit
    template_name = 'swjoke/detail.html'
    context_object_name = 'object'






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
        if bound_form.is_valid():
            new_recruit = bound_form.save()
            base_url = reverse('swjoke:black_test')
            query_string =  urlencode({'recruit_id': new_recruit.pk })
            url = f'{base_url}?{query_string}'
            return redirect(url)
        return render(request, 'swjoke/new_recruit.html', context={'form' : bound_form})

