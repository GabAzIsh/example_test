from django.test import TestCase
from swjoke.forms import RecruitForm, AnswerForm


class TestForms(TestCase):
    fixtures = ['swjoke.json']
    def test_recruit_form_valid(self):
        post={
            'recruit_planet' : 1,
            'recruit_name' : 'Charles',
            'recruit_age' : 35,
            'recruit_email' : 'crowling@gmail.com'
        }
        form = RecruitForm(post)

        self.assertTrue(form.is_valid())

    def test_recruit_form_is_empty(self):
        form = RecruitForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_answer_form_valid(self):
        post={
            'answer' : 'yes',
            'question' : 1,
            'recruit' : 35,
        }
        form = AnswerForm(post)

        self.assertTrue(form.is_valid())

    def test_answer_form_title(self):
        post={
            'answer' : 'yes',
            'question' : 1,
            'recruit' : 35,
        }
        form = AnswerForm(data=post, initial={'title': 'romb'})
        self.assertEqual(form.title, 'romb')

    def test_answer_form_no_title(self):
        post={
            'answer' : 'yes',
            'question' : 1,
            'recruit' : 35,
        }
        form = AnswerForm(data=post)
        self.assertFalse(form.title)
