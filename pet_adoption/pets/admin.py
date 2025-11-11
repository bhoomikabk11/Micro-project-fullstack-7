from django.contrib import admin
from .models import Pet, Contact, PetContact

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'age', 'uploaded_by', 'owner_name', 'owner_email']
    list_filter = ['breed', 'uploaded_by']
    search_fields = ['name', 'breed', 'owner_name', 'owner_email', 'uploaded_by__username']
    fieldsets = (
        ('Pet Information', {
            'fields': ('name', 'age', 'breed', 'description', 'image')
        }),
        ('Upload Information', {
            'fields': ('uploaded_by',)
        }),
        ('Owner Information', {
            'fields': ('owner_name', 'owner_email', 'owner_phone')
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']

@admin.register(PetContact)
class PetContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'pet', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at', 'pet']
    search_fields = ['name', 'email', 'phone', 'message', 'pet__name']
    readonly_fields = ['created_at', 'pet']
    list_editable = ['is_read']
    fieldsets = (
        ('Contact Information', {
            'fields': ('pet', 'name', 'email', 'phone', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
