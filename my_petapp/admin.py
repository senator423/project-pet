from django.contrib import admin
from .models import BlogPost, Booking, Contact, Service, ContactMessage


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'date', 'time')
    search_fields = ('name', 'email', 'service')
    list_filter = ('date', 'service')
    ordering = ('-date',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    ordering = ('-submitted_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
