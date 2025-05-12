from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('events/', views.events, name='events'),
    # path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/update/<int:pk>/', views.update_feedback, name='update_feedback'),
    path('feedback/delete/<int:pk>/', views.delete_feedback, name='delete_feedback'),
    # path('send-email/', views.send_email_view, name='send_email'),
    path('event_booking_list/', views.event_booking_list, name='event_booking_list'),
    path('terms/', views.terms, name='terms'), 
    path('privacy/', views.privacy, name='privacy'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('booking_view/', views.booking_view, name='booking_view'),
    path('about/', views.about, name='about'),
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/confirmation/<int:pk>/', views.booking_confirmation, name='event_booking_confirmation'),
]   
