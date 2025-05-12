from django.contrib import admin
from .models import Event, Booking, Feedback, TeamMember


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'desc', 'img')
    search_fields = ('name', 'category', 'desc')
    list_filter = ('category',)
    ordering = ('name',)
    list_per_page = 20


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'payment_price', 'booked_on', 'payment_description')
    search_fields = ('name', 'email')  # Fixed: 'name__name' only works if name is FK
    list_filter = ('booked_on',)  # Removed 'payment_price'
    ordering = ('-booked_on',)



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    ordering = ('-id',)
    list_per_page = 20


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'photo')
    search_fields = ('name', 'role', 'bio')
    list_filter = ('role',)
    ordering = ('name',)
    list_per_page = 20
