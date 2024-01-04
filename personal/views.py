
from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = 'personal/profile.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
