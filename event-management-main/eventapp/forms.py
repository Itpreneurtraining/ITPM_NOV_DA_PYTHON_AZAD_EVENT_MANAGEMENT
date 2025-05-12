from django import forms
from .models import Event, Booking, Feedback, TeamMember


# ----------- Date Picker Input -----------
class DateInput(forms.DateInput):
    input_type = 'date'


# ----------- Event Form -----------
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['img', 'name', 'desc', 'category', 'price']
        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short Description'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Event Price'}),
        }
        labels = {
            'img': 'Event Image',
            'name': 'Event Name',
            'desc': 'Description',
            'category': 'Category',
            'price': 'Price (₹)',
        }


# ----------- Booking Form -----------
class BookingForm(forms.ModelForm):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    ]

    payment_status = forms.ChoiceField(
        choices=PAYMENT_STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,  # You may want to auto-set this in views
        label="Payment Status"
    )

    class Meta:
        model = Booking
        fields = [
            'event',
            'name',
            'email',
            'phone',
            'payment_price',
            'payment_description',
            'payment_method',
            'payment_status',
        ]
        widgets = {
            'event': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'payment_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'payment_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details', 'rows': 3}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Payment Method'}),
        }
        labels = {
            'event': 'Select Event',
            'name': 'Customer Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'payment_price': 'Payment Amount',
            'payment_description': 'Payment Details',
            'payment_method': 'Payment Method',
        }


# ----------- Feedback Form -----------
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
            'rating': forms.RadioSelect(attrs={'class': 'rating-stars'}, choices=[(i, '⭐' * i) for i in range(1, 6)]),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'message': 'Message',
            'rating': 'Rating',
        }

# ----------- Team Member Form -----------
class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'photo', 'bio']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role/Position'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Short Bio', 'rows': 3}),
        }
        labels = {
            'name': 'Team Member Name',
            'role': 'Role / Position',
            'photo': 'Photo',
            'bio': 'Biography',
        }
