from datetime import timedelta

from django import forms
from django.conf import settings
from django.forms import ValidationError

from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.template.loader import get_template

from .models import MagicLink

USER_MODEL = get_user_model()

MAGICADMIN_DEFAULT_EXPIRATION = getattr(
    settings,
    "MAGICADMIN_DEFAULT_EXPIRATION",
    10800
)
MAGICADMIN_DEFAULT_MAGIC_LINK_SUBJECT = getattr(
    settings,
    "MAGICADMIN_DEFAULT_MAGIC_LINK_SUBJECT",
    "Here is your magic link to login!"
)

MAGICADMIN_CURRENT_WEBSITE = getattr(
    settings,
    "MAGICADMIN_CURRENT_WEBSITE",
    "localhost"
)
MAGICADMIN_DEFAULT_SENDER_EMAIL = getattr(
    settings,
    "MAGICADMIN_DEFAULT_SENDER_EMAIL",
    "magiclink@localhost"
)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=1000)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")

        queryset = USER_MODEL.objects.filter(username=username)

        if queryset.count() == 0:
            raise ValidationError("Username not found!")

        self.user = queryset.first()

        return cleaned_data
    
    def _generate_magic_link(self):
        self.user_magiclink = MagicLink.objects.create(
            user = self.user,
        )
        self.user_magiclink.expires_at = self.user_magiclink.created_at + timedelta(
            seconds=MAGICADMIN_DEFAULT_EXPIRATION
        )
        self.user_magiclink.save()

    def send_magic_link(
            self,
            request,
            text_template="emails/magiclogin.txt",
            html_template="emails/magiclogin.html",
            custom_context = {},
        ):

        context = custom_context
        self._generate_magic_link()
        context["site"] = MAGICADMIN_CURRENT_WEBSITE
        context["magiclink"] = self.user_magiclink.get_login_url(request=request)

        plain_text = get_template(text_template)
        html_text = get_template(html_template)

        text_content, html_content = plain_text.render(context), html_text.render(context)

        subject = MAGICADMIN_DEFAULT_MAGIC_LINK_SUBJECT
        receiver = self.user.email
        msg = EmailMultiAlternatives(
            subject, text_content, MAGICADMIN_DEFAULT_SENDER_EMAIL, [receiver]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()