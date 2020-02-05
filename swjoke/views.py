from django.shortcuts import get_object_or_404,redirect, render
from django.views import generic, View
# Create your views here.
from .models import Recruit, Sith, SithPlanets, Test
from .forms import RecruitForm

class IndexView(generic.ListView):
    template_name = 'swjoke/test.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """
        Return random five  questions.
        """
        return Test.objects.order_by('?')[:3]

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
        print(request.POST)
        if bound_form.is_valid():
            new_recruit = bound_form.save()
            return redirect(new_recruit)
        return render(request, 'swjoke/new_recruit.html', context={'form' : bound_form})
