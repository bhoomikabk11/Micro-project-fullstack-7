from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Pet, Contact, PetContact  # import the models

User = get_user_model()

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet  # link this form to the Pet model
        fields = ['name', 'age', 'breed', 'description', 'image', 'owner_name', 'owner_email', 'owner_phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Pet Name',
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age in months',
            }),
            'breed': forms.TextInput(attrs={
                'placeholder': 'Breed',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Pet description...',
                'rows': 4,
            }),
            'owner_name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
            }),
            'owner_email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
            }),
            'owner_phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number (Optional)',
            }),
        }
        labels = {
            'age': 'Age (in months)',
            'owner_name': 'Owner Name',
            'owner_email': 'Owner Email',
            'owner_phone': 'Owner Phone (Optional)',
        }
        help_texts = {
            'owner_name': 'Name of the pet owner',
            'owner_email': 'Email address to contact the owner',
            'owner_phone': 'Phone number (optional)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner_name'].required = True
        self.fields['owner_email'].required = True
        # Move help text to appear before the field
        for field_name, field in self.fields.items():
            if field.help_text:
                field.widget.attrs['title'] = field.help_text

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message here...',
                'rows': 6,
                'class': 'form-control'
            }),
        }

class PetContactForm(forms.ModelForm):
    class Meta:
        model = PetContact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number (Optional)',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message to the owner...',
                'rows': 6,
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'your.email@example.com',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Email or Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email or Username',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )