from django.shortcuts import render
from rest_framework import generics
from .models import Service, Booking, BlogPost, ContactMessage
from .serializers import ServiceSerializer, BookingSerializer, BlogPostSerializer, ContactSerializer
from .models import Contact

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def pricing(request):
    return render(request, 'price.html')

def booking_page(request):
    return render(request, 'booking.html')

def blog_list_page(request):
    return render(request, 'blog.html')

def contact_page(request):
    return render(request, 'contact.html')
# Service API
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Booking API
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Blog API
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Contact API
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
