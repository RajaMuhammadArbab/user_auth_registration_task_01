from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email'] 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        
        
        full_name = self.cleaned_data.get('full_name')
        if full_name:
            parts = full_name.strip().split(None, 1)
            user.first_name = parts[0]
            user.last_name = parts[1] if len(parts) > 1 else ''

        user.email = self.cleaned_data.get('email')
        user.username = self.cleaned_data.get('email')  

        if commit:
            user.save()
        return user
