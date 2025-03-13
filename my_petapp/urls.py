from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/update/<int:post_id>/', views.blog_update, name='blog_update'),
    path('blog/delete/<int:post_id>/', views.blog_delete, name='blog_delete'),
    path('booking/', views.booking_list, name='booking_list'),
    path('booking/create/', views.booking_create, name='booking_create'),
    path('contact/', views.contact_view, name='contact'),
]
