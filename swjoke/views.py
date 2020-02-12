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


''' def mail_sand
send_mail('Text of email subject. Example: From Django swjoke Sith'
    'text of email',
    'captain_taylor@list.ru'
    ['address of mail receiver/recepient'],
    fail_silently=False)


'''
# def index(request):
#     recipients=['kino89@list.ru']
#     subject='From Django swjoke Sith'
#     message='text of email'
#     sender='captain.justy.ueki.taylor@gmail.com'
#     send_mail(subject, message, sender, recipients)
#     return HttpResponse('Sended')
class IndexView(TemplateView):
    template_name = 'swjoke/index.html'

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
            send_mail(
                'Text of email subject. Example: From Django swjoke Sith', 
                'text of email', 
                'captain_taylor@list.ru', 
                [recruit.recruit_email], 
                fail_silently=False, 
                )

    def dispatch(self, request, *args, **kwargs):
        self.planet_id = kwargs['planet_sith_id']
        self.sith_id = kwargs['sith_id']
        if request.method == 'POST':
            self.recruit_id = request.POST.get("recruit_id")
            self.record_shadow_hand(self.recruit_id, self.sith_id)

        return super().dispatch(request, *args, **kwargs)

    # url = 'swjoke/recruit-list/%(planet_sith_id)/%(sith_id)/'
    pattern_name = 'swjoke:recruit_list'
    permanent = False
    query_string = True



class RecruitList(generic.ListView):

    def dispatch(self, request, *args, **kwargs): 
        self.planet_id = kwargs['planet_sith_id']
        self.sith_id = kwargs['sith_id']
        print(int(self.sith_id))
        print(Sith.objects.get(id = int(self.sith_id)))
        if len(Sith.objects.get(id = int(self.sith_id)).recruit_set.all()) >= 3:
            return render(request, 'swjoke/index.html')
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
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
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
            return render(request, 'swjoke/index.html')
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

