from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template import Context, Template
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings


def logout_view(request):
    logout(request)
    return redirect("home")

