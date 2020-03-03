from django.test import SimpleTestCase
from django.urls import reverse, resolve
from swjoke import views

'''
    path('', views.IndexView.as_view(), name='index'),
    path('test/', views.RecruitCreate.as_view(), name='test'),
    path('<int:pk>/detail/', views.RecruitDetailView.as_view(), name='detail'),
    path('black_test/', views.BlackTest.as_view(), name='black_test'),
    path('sith/', views.SithList.as_view(), name='sith_list'),
    path('recruit-list/<int:planet_sith_id>/<int:sith_id>/', views.RecruitList.as_view(), name='recruit_list'),
    path('redirect/<int:sith_id>/<int:planet_sith_id>/', views.SithUpdateRedirect.as_view(), name='redirect'),
    '''


class TestView(SimpleTestCase):

# Main page view resolve testing
    def test_index_url_is_resolved(self):
        url = reverse('swjoke:index')
     #   print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, views.IndexView)

# Recruit create view resolve testing
    def test_test_url_is_resolved(self):
        url = reverse('swjoke:test')
        self.assertEqual(resolve(url).func.view_class, views.RecruitCreate)

# Detail View of recruit resolve testing
    def test_detail_url_is_resolved(self):
        url = reverse('swjoke:detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.RecruitDetailView)

# View of questionnaire resolve testing
    def test_black_test_url_is_resolved(self):
        url = reverse('swjoke:black_test')
        self.assertEqual(resolve(url).func.view_class, views.BlackTest)

# View of Sith list resolve testing
    def test_sith_list_url_is_resolved(self):
        url = reverse('swjoke:sith_list')
        self.assertEqual(resolve(url).func.view_class, views.SithList)

# View of recruit list resolve testing 
    def test_recruit_list_url_is_resolved(self):
        url = reverse('swjoke:recruit_list', args=[1, 1])
        self.assertEqual(resolve(url).func.view_class, views.RecruitList)

# Redirection for the sith models updating resolve testing
    def test_redirect_url_is_resolved(self):
        url = reverse('swjoke:redirect', args=[1, 1])
        self.assertEqual(resolve(url).func.view_class, views.SithUpdateRedirect)