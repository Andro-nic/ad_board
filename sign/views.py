from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.urls import reverse_lazy

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('announcement_list')
