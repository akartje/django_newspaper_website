from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class ArticleTest(TestCase):
	def test_article_create_form(self):
		response = self.client.post(
			reverse('article_create'),
			{
				'title': 'test_title',
				'body': 'test_body',
			},
		)
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		self.assertEqual(get_user_model().objects.all()[0].title, 'test_title')
		self.assertEqual(get_user_model().objects.all()[0].body, 'test_body')
		
		response2 = self.client.get("/1/")
		self.assertEqual(response2.status_code, 200)
