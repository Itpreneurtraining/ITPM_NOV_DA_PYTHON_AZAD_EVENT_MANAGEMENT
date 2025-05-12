from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User


class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Occasions', 'Occasions'),
        ('Parties', 'Parties'),
        ('Functions', 'Functions'),
    ]
    
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Fixed price for the event
    

    def recent_bookings(self):
        """Returns the 5 most recent bookings for the event."""
        return self.bookings.order_by('-booked_on')[:5]  # Use 'bookings' instead of 'booking_set'

    def total_bookings(self):
        """Returns the total number of bookings for the event."""
        return self.bookings.count()  # Use 'bookings' instead of 'booking_set'

    def total_revenue(self):
        """Returns the total revenue for the event based on completed bookings."""
        return sum(booking.payment_price for booking in self.bookings.filter(payment_status='Paid'))

    def __str__(self):
        return self.name


class Booking(models.Model):
    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    payment_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_description = models.TextField()
    payment_method = models.CharField(max_length=50)
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.event.name} by {self.name}"



class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(default=0)  # Star rating: 1 to 5

    def __str__(self):
        return f"{self.name} - {self.rating} stars"

    # def __str__(self):
    #     return f"Feedback from {self.name}"


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
