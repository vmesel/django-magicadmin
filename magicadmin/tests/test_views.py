from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from magicadmin.models import MagicLink

User = get_user_model()

class MagicLinkViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.client = Client()


    def test_admin_login_is_loaded_correctly(self):
        response = self.client.get('/admin/', follow=True)

        self.assertNotIn(b"password", response)
