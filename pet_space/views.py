from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegistrationView(CreateView):
    template_name = "registration/registration_form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home:homepage')
