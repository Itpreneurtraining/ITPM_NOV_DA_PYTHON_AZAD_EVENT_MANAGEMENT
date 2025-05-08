from django.shortcuts import render,redirect
from . models import Event
from .forms import BookingForm
# Create your views here.
from django.shortcuts import render
from .models import Event, Booking

# def index(request):
#     eve = Event.objects.all()
#     bookings = Booking.objects.select_related('name').all()
#     return render(request, 'index.html', {'eve': eve, 'bookings': bookings})

from django.shortcuts import render
from .models import Event, Booking

def index(request):
    eve = Event.objects.all()
    recent_bookings = Booking.objects.select_related('name').order_by('-booked_on')[:5]
    return render(request, 'index.html', {'eve': eve, 'recent_bookings': recent_bookings})


def about(request):
    return render(request,'about.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')





from django.shortcuts import render
from .models import Event, Booking

def recent_bookings_per_event(request):
    events = Event.objects.all()

    for event in events:
        event.recent_bookings = Booking.objects.filter(name=event).order_by('-booked_on')[:3]

    return render(request, 'recent_bookings_list.html', {'eve': events})


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

def send_email_view(request):
    try:
        send_mail(
            subject='Test Email',
            message='This is a test email from Django.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['your_test_email@example.com'],
            fail_silently=False,
        )
        return HttpResponse('Email sent successfully!')
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        return HttpResponse(f'Error occurred: {e}')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from .forms import FeedbackForm

def feedback_view(request):
    form = FeedbackForm(request.POST or None)
    feedbacks = Feedback.objects.all().order_by('-id')
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('feedback')
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})

def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    form = FeedbackForm(request.POST or None, instance=feedback)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('feedback')
    return render(request, 'update_feedback.html', {'form': form})

def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback')
    return render(request, 'delete_feedback.html', {'feedback': feedback})
