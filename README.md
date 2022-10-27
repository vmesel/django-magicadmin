# Django Magic Admin

This is a plugin to facilitate django-admin login through magic links.

## Requirements

 - Django 4.X or higher
 - An E-mail service provider such as SMTP, Sendgrid or others configured on settings.py

## Installation

 - `pip install django-django_magicadmin` on your system
 - Add the following URL and include it in your main `urls.py`

```
path("", include("django_magicadmin.urls")),
```
 - Add the app to your INSTALLED_APPS
```
INSTALLED_APPS = [
    "django_magicadmin",
    ...
]
```
 - If you want custom settings about Sender address, Domain, etc, use the following fields and add them to your settings.py:

```
MAGICADMIN_DEFAULT_EXPIRATION = 10800 # default
MAGICADMIN_DEFAULT_MAGIC_LINK_SUBJECT = "Here is your magic link to login!" # default
MAGICADMIN_CURRENT_WEBSITE = localhost
MAGICADMIN_DEFAULT_SENDER_EMAIL = magiclink@localhost
```

### Pro tips:

Here are some tips that will enable a better experience for you

#### Pro tip #1:
If you want to develop using the magic link functionality, I recommend you
the Django Terminal E-mail Backend, which enables you to see all of the messages sent through the system.

Just add this one-liner to your settings.py:

```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```


#### Pro tip #2:
To override with custom e-mail templates, override the files: `emails/magiclogin.html` and `emails/magiclogin.txt`