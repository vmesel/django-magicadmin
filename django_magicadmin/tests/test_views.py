from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from django_magicadmin.models import MagicLink

User = get_user_model()

class MagicLinkViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            email="user@gmail.com",
            password="password",
            is_superuser=True,
            is_staff=True
        )
        self.client = Client()
        self.auth_client = Client()
        self.auth_client.login(username="user", password="password")

    def test_admin_login_is_loaded_correctly(self):
        response = self.client.get('/admin/login/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertNotIn("password", response.content.decode("utf-8"))

    def test_access_home_when_logged_in(self):
        response = self.auth_client.get('/admin/login/', follow=True)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertIn("Welcome,", response.content.decode("utf-8"))

    def test_get_magic_link_page(self):
        ml = MagicLink.objects.create(
            user = self.user,
            already_used = True
        )
        login_url = ml.get_login_url(complete=False)
        response = self.client.get(f'{login_url}', follow=True)
        self.assertIn(
            "/admin/login/?next=/admin/login%3Falready_used%3Dtrue",
            response.redirect_chain[-1][0]
        )

