
from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = 'personal/profile.html'
    context_object_name = 'profile'