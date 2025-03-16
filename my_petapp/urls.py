from django.urls import path
from .views import (
    ServiceListCreateView, ServiceDetailView,
    BookingListCreateView, BookingDetailView,
    BlogPostListCreateView, BlogPostDetailView,
    ContactListCreateView, index, about, services, pricing, booking_page, blog_list_page, contact_page
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('pricing/', pricing, name='pricing'),
    path('booking/', booking_page, name='booking'),
    path('blog/', blog_list_page, name='blog'),
    path('contact/', contact_page, name='contact'),

    path('api/services/', ServiceListCreateView.as_view(), name='api_service_list'),
    path('api/services/<int:pk>/', ServiceDetailView.as_view(), name='api_service_detail'),

    path('api/bookings/', BookingListCreateView.as_view(), name='api_booking_list'),
    path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='api_booking_detail'),

    path('api/blog/', BlogPostListCreateView.as_view(), name='api_blog_list'),
    path('api/blog/<int:pk>/', BlogPostDetailView.as_view(), name='api_blog_detail'),

    path('api/contact/', ContactListCreateView.as_view(), name='api_contact_list'),
]
