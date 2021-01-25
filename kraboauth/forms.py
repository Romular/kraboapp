from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User, UserProfile
from datetime import datetime, date
from django.utils import timezone
from django.db.models import Q, Sum
from django.forms import PasswordInput


class GeAuthLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control form-control-navbar', 'placeholder': _('Username')}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control form-control-navbar', 'placeholder': _('Password')}),
    )


