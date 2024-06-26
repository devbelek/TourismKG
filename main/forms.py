from allauth.account.forms import SignupForm
from django import forms
from .models import Tour, UserRegistration, GuideRegistration


class CustomSignupForm(SignupForm):
    Role_CH = (
        ('regular', 'Regular'),
        ('guide', 'Guide'),
    )
    role = forms.ChoiceField(choices=Role_CH, required=True)
    bio = forms.CharField(widget=forms.Textarea, required=True)
    experience = forms.CharField(max_length=300, required=True)
    phone_number = forms.IntegerField(required=True)
    image = forms.ImageField(required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        role = self.cleaned_data.get('role')
        bio = self.cleaned_data.get('bio')
        experience = self.cleaned_data.get('experience')
        phone_number = self.cleaned_data.get('phone_number')
        image = self.cleaned_data.get('image')

        if role == 'guide':
            GuideRegistration.objects.create(
                user=user,
                bio=bio,
                experience=experience,
                phone_number=phone_number,
                image=image
            )
        elif role == 'regular':
            UserRegistration.objects.create(
                user=user,
            )
        return user


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['title', 'description', 'start_date', 'end_date', 'price', 'location']