from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    # User who uploaded this pet
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_pets', null=True, blank=True)
    # Owner contact information
    owner_name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the pet owner")
    owner_email = models.EmailField(blank=True, null=True, help_text="Email address to contact the owner")
    owner_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Phone number (optional)")

    def __str__(self):
        return self.name
    
    def can_edit(self, user):
        """Check if user can edit this pet"""
        if not user.is_authenticated:
            return False
        if user.is_superuser or user.is_staff:
            return True
        return self.uploaded_by == user

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.subject}"

class PetContact(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='contact_requests')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Pet Contact Request'
        verbose_name_plural = 'Pet Contact Requests'

    def __str__(self):
        return f"{self.name} - {self.pet.name}"