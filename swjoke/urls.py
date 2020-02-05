from django.urls import path

from . import views

app_name = 'swjoke'
urlpatterns = [
    path('test/', views.IndexView.as_view(), name='test'),
    path('<int:pk>/detail/', views.RecruitDetailView.as_view(), name='detail'),
    path('<int:pk>/detail/', views.SithDetailView.as_view(), name='detail'),
    path('new/', views.RecruitCreate.as_view(), name='new_recruit_url'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
   # path('<int:question_id>/vote/', views.vote, name='vote'),'''
]