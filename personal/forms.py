from django import forms
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()

class UserProfileForm(forms.ModelForm):

    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = (
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'sex',
            'avatar',
        )