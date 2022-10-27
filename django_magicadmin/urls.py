from django_magicadmin.views import *
from django.urls import path

urlpatterns = [
    path("admin/login/", login_view, name="magic_login_index"),
    path("admin/login/validate/<str:magiclink>/", authenticate_view, name="magic_login_validate"),
]
