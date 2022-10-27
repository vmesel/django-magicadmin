from django.test import TestCase
from django.contrib.auth import get_user_model

from django_magicadmin.models import MagicLink

User = get_user_model()

class MagicLinkModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")

    def test_model_creates(self):
        ml = MagicLink.objects.create(user=self.user)

        self.assertIn(ml, MagicLink.objects.all())