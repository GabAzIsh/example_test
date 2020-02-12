from django.urls import path

from . import views

app_name = 'swjoke'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/', views.RecruitCreate.as_view(), name='test'),
    path('<int:pk>/detail/', views.RecruitDetailView.as_view(), name='detail'),
    #path('<int:pk>/detail/', views.SithDetailView.as_view(), name='detail'),
    path('new/', views.RecruitCreate.as_view(), name='new_recruit_url'),
    path('black_test/', views.BlackTest.as_view(), name='black_test'),
    path('sith/', views.SithList.as_view(), name='sith_list'),
    path('recruit-list/<int:planet_sith_id>/<int:sith_id>/', views.RecruitList.as_view(), name='recruit_list'),
    path('redirect/<int:sith_id>/<int:planet_sith_id>/', views.SithUpdateRedirect.as_view(), name='redirect'),
]