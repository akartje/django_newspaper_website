from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class HomePageTests(SimpleTestCase):
	def test_url_exists_at_correct_location_signupview(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)
		
	def test_homepage_view_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')
		self.assertContains(response, 'Home')
