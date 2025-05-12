from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_event, name='book_event'),
    path('my_view/', views.my_view, name='my_view'),
    # path('', views.home, name='home'),  # assuming you have a homepage
]
