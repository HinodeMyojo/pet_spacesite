from django.db.models.base import Model as Model
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model
from datetime import date
from dateutil.relativedelta import relativedelta
from .forms import UserProfileForm

User = get_user_model()

def calculate_age(date_birth):
    if date_birth == 0 or None:
        return 0
    else:
        today = date.today()
        age = relativedelta(today, date_birth)
        age = age.years
        return age

class UserProfileDetailView(DetailView):
    model = User
    form_class = UserProfileForm
    template_name = 'personal/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_birth = context['profile'].date_birth
        context["age"] = calculate_age(date_birth) 
        return context
    

class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'personal/edit.html'

    def get_object(self, queryset) -> Model:
        return self.request.user
