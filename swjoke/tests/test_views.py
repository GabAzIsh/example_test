from django.core import mail
from django.test import TestCase, Client
from django.urls import reverse
from swjoke import models

import json
from urllib.parse import urlencode
# for executing Selenium                browser = webdriver.Firefox(executable_path='C:\geckodriver.exe')
class TestViews(TestCase):
    fixtures = ['swjoke.json']
    def setUp(self):
        self.client = Client()
        self.index_view_url = reverse('swjoke:index')
        self.recruit_create_url = reverse('swjoke:test')
        self.recruit_detail_view_url = reverse('swjoke:detail', args=[36])
        
        black_test_url = reverse('swjoke:black_test')
        query_string =  urlencode({'recruit_id': 36 })
        self.black_test_url = f'{black_test_url}?{query_string}'

        self.sith_list_url = reverse('swjoke:sith_list')
        self.recruit_list_url = reverse('swjoke:recruit_list', args=[1, 1])      
        self.sith_update_redirect_url = reverse('swjoke:redirect', args=[1, 1])


# GET requests

# IndexView view
    def test_indexview_GET(self):
        response = self.client.get(self.index_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/index.html')
# RecruitCreate view
    def test_recruit_create_GET(self):
        response = self.client.get(self.recruit_create_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/new_recruit.html')
# RecruitDetailView view
    def test_recruit_detail_view_GET(self):
        response = self.client.get(self.recruit_detail_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/detail.html')
# BlackTest view
    def test_black_test_GET(self):
        response = self.client.get(self.black_test_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/black_test.html')
# SithList view
    def test_sith_list_test_GET(self):
        response = self.client.get(self.sith_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/sith_list.html')
# RecruitList view
    def test_recruit_list_test_GET(self):
        response = self.client.get(self.recruit_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/recruit_list.html')  


    def test_recruit_list_test_GET_limit(self):
        response = self.client.get(reverse('swjoke:recruit_list', args=[2, 3]))
        text = 'You have reached maximum number of Shadow Hand'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/index.html')  
        self.assertContains(response, text)
        
             

        
# SithUpdateRedirect view
    def test_sith_update_redirect_test_GET(self):
        response = self.client.get(self.sith_update_redirect_url, follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/recruit_list.html')    


## POST

# BlackTest view
    def test_black_test_POST(self):
        response = self.client.post(self.black_test_url, {
            'form-TOTAL_FORMS': ['3'], 
            'form-INITIAL_FORMS': ['3'], 
            'form-MIN_NUM_FORMS': ['0'], 
            'form-MAX_NUM_FORMS': ['1000'], 
            'form-0-answer': ['yes'], 
            'form-0-question': ['1'], 
            'form-0-recruit': ['36'], 
            'form-1-answer': ['yes'], 
            'form-1-question': ['2'], 
            'form-1-recruit': ['36'], 
            'form-2-answer': ['no'], 
            'form-2-question': ['3'], 
            'form-2-recruit': ['36']
        })
        text = 'You personal information was sucsefully registrated. Sith decision will be sended to you later'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/index.html')
        self.assertContains(response, text, status_code=200)


# RecruitCreate view
    def test_recruit_create_POST(self):
        response = self.client.post(self.recruit_create_url,{
            'recruit_planet' : 1,
            'recruit_name' : 'Charles',
            'recruit_age' : 35,
            'recruit_email' : 'crowling@gmail.com'
        }, follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/black_test.html')


    def test_recruit_create_POST_no_data(self):
        response = self.client.post(self.recruit_create_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/new_recruit.html')

# SithUpdateRedirect view
    def test_sith_update_redirect_test_POST(self):
        response = self.client.post(self.sith_update_redirect_url,{
            "recruit_id" : 40
        }, follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'swjoke/index.html')    






class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')