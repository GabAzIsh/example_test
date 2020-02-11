from django.urls import path

from . import views

app_name = 'swjoke'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/', views.RecruitCreate.as_view(), name='test'),
    path('<int:pk>/detail/', views.RecruitDetailView.as_view(), name='detail'),
    #path('<int:pk>/detail/', views.SithDetailView.as_view(), name='detail'),
    path('new/', views.RecruitCreate.as_view(), name='new_recruit_url'),
    path('create/', views.RecruitCreateView.as_view(), name='simple_create_url'),
    path('black_test/', views.Romb.as_view(), name='black_test'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # 
    # 
    #path('shadow_hand_test/', views.ShadowHand.as_view(), name='shadow_hand_test')
]