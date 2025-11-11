from django.urls import path
from . import views

urlpatterns = [
    path('', views.available_pets, name='available_pets'),  # Home page shows pets
    path('upload/', views.upload_pet, name='upload_pet'),   # Upload page
    path('contact/', views.contact_us, name='contact_us'),  # Contact Us page
    path('pet/<int:pet_id>/contact/', views.contact_owner, name='contact_owner'),  # Contact pet owner
    path('pet/<int:pet_id>/edit/', views.edit_pet, name='edit_pet'),  # Edit pet
    path('pet/<int:pet_id>/delete/', views.delete_pet, name='delete_pet'),  # Delete pet
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # Custom login view
]