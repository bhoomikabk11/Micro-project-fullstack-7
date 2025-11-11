from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Pet
from .forms import PetForm, ContactForm, PetContactForm, CustomUserCreationForm, CustomAuthenticationForm

def available_pets(request):
    # Show all pets to everyone (for browsing)
    # But edit/delete buttons will only show for owners/admins
    pets = Pet.objects.all()
    return render(request, 'pets/available.html', {'pets': pets})

@login_required
def upload_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.uploaded_by = request.user
            pet.save()
            messages.success(request, 'Pet uploaded successfully!')
            return redirect('available_pets')
    else:
        form = PetForm()
    return render(request, 'pets/upload.html', {'form': form})

@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    # Check if user has permission to edit this pet
    if not pet.can_edit(request.user):
        messages.error(request, 'You do not have permission to edit this pet.')
        return redirect('available_pets')
    
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, f'{pet.name} has been updated successfully!')
            return redirect('available_pets')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/edit.html', {'form': form, 'pet': pet})

@login_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    # Check if user has permission to delete this pet
    if not pet.can_edit(request.user):
        messages.error(request, 'You do not have permission to delete this pet.')
        return redirect('available_pets')
    
    if request.method == 'POST':
        pet_name = pet.name
        pet.delete()
        messages.success(request, f'{pet_name} has been deleted successfully.')
        return redirect('available_pets')
    return render(request, 'pets/delete.html', {'pet': pet})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'pets/contact.html', {'form': form})

@login_required
def contact_owner(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    # Check if owner email is available
    if not pet.owner_email:
        messages.error(request, 'Owner contact information is not available for this pet.')
        return redirect('available_pets')
    
    if request.method == 'POST':
        form = PetContactForm(request.POST)
        if form.is_valid():
            pet_contact = form.save(commit=False)
            pet_contact.pet = pet
            pet_contact.save()
            
            # Send email to pet owner
            try:
                owner_name = pet.owner_name if pet.owner_name else 'Pet Owner'
                subject = f'New Inquiry About {pet.name} - Pet Adoption'
                
                message_body = f"""
Hello {owner_name},

You have received a new inquiry about {pet.name} ({pet.breed}) from the Pet Adoption website.

Contact Details:
- Name: {pet_contact.name}
- Email: {pet_contact.email}
{f'- Phone: {pet_contact.phone}' if pet_contact.phone else ''}

Message:
{pet_contact.message}

---
This message was sent through the Pet Adoption website.
Please reply directly to {pet_contact.email} to respond to this inquiry.

Thank you!
Pet Adoption Team
"""
                
                send_mail(
                    subject=subject,
                    message=message_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[pet.owner_email],
                    fail_silently=False,
                )
                
                owner_name = pet.owner_name if pet.owner_name else 'the owner'
                messages.success(request, f'Your message has been sent to {owner_name}! They will contact you soon.')
            except Exception as e:
                # If email fails, still save the contact but show a warning
                messages.warning(request, f'Your message has been saved, but there was an issue sending the email. The owner will be notified through the website.')
            
            return redirect('available_pets')
    else:
        form = PetContactForm()
    return render(request, 'pets/contact_owner.html', {'form': form, 'pet': pet})

def logout_view(request):
    """Custom logout view that handles GET requests"""
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
    return redirect('available_pets')

def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('available_pets')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Specify the backend when logging in
            from django.contrib.auth import get_backends
            backend = 'django.contrib.auth.backends.ModelBackend'
            user.backend = backend
            login(request, user, backend=backend)
            messages.success(request, f'Welcome {user.username}! Your account has been created successfully.')
            return redirect('available_pets')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pets/register.html', {'form': form})

def login_view(request):
    """Custom login view that uses email authentication"""
    if request.user.is_authenticated:
        return redirect('available_pets')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('available_pets')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'Registration/login.html', {'form': form})