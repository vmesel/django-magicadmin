from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from magicadmin.models import MagicLink

User = get_user_model()

class MagicLinkViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.client = Client()
        self.auth_client = Client()
        self.auth_client.login(username="user", password="password")


    def test_admin_login_is_loaded_correctly(self):
        response = self.client.get('/admin/login/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertNotIn("password", response.content.decode("utf-8"))

    def test_access_home_when_logged_in(self):
        response = self.auth_client.get('/admin/password_change/', follow=True)
        
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertIn("Welcome, user", response.content.decode("utf-8"))
