from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from .forms import CustonUserChangeForm

User = get_user_model()

class CustomUserUpdateView(UpdateView):
    model = User
    form_class = CustonUserChangeForm
    template_name = 'personal/profile.html'
    context_object_name = 'profile'