from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'position', 'place']

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        image_file = self.cleaned_data.get('profile_picture')

        # Save the base64-encoded image if provided
        if image_file:
            user_profile.set_profile_picture(image_file)

        if commit:
            user_profile.save()
            user = user_profile.user
            user.username = self.cleaned_data['name']
            user.email = self.cleaned_data['email']
            user.save()
        return user_profile
