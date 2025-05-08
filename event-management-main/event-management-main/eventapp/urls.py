from django.urls import path
from .views import (
    index, about, events, booking, contact,
    recent_bookings_per_event, send_email_view,
    feedback_view, update_feedback, delete_feedback
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('recent_bookings_per_event/', recent_bookings_per_event, name='recent_bookings_per_event'),
    path('send-email/', send_email_view, name='send_email'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback/update/<int:pk>/', update_feedback, name='update_feedback'),
    path('feedback/delete/<int:pk>/', delete_feedback, name='delete_feedback'),
]
