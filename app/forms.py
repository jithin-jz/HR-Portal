from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile

# Form for editing profile
class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'position', 'place']

    def save(self, commit=True):
        user_profile = super().save(commit)
        user = User.objects.get(username=user_profile.user.username)
        user.username = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user_profile
