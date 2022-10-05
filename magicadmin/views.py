from .models import MagicLink
from .forms import LoginForm
from datetime import datetime

from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

def login_view(request):
    form = LoginForm(request.POST or None)
    already_used = True if request.GET.get('already_used', None) else False

    context = {
        "form": form,
        "custom_error_message": already_used
    }

    if request.user.is_authenticated:
        return redirect("/admin/")

    if request.method != 'POST' or not form.is_valid():
        return render(request, 'login.html', context=context)
    
    form.send_magic_link(request)

    context['success_message'] = "E-mail sent to the user's email address"

    return render(request, 'login.html', context=context) 


def authenticate_view(request, magiclink):
    instance = get_object_or_404(MagicLink, secret_identifier = magiclink)

    if instance.already_used or (instance.expires_at.timestamp() < datetime.now().timestamp()):
        return redirect("/admin/login?already_used=true")
    
    instance.already_used = True
    instance.used_at = datetime.now()
    instance.save()

    login(request, instance.user)
    return redirect("/admin/")

    