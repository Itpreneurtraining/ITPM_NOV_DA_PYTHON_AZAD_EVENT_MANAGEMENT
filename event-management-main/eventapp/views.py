from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Event, Booking, Feedback, TeamMember
from .forms import BookingForm, FeedbackForm
from django.http import HttpResponseForbidden


def index(request):
    eve = Event.objects.all()
    recent_bookings = Booking.objects.order_by('-booked_on')[:5]
    return render(request, 'index.html', {'eve': eve, 'recent_bookings': recent_bookings})


@login_required(login_url='login')
def events(request):
    categories = ['Occasions', 'Parties', 'Functions']
    categorized_events = {cat: Event.objects.filter(category=cat) for cat in categories}
    return render(request, 'events.html', {'categorized_events': categorized_events})


def contact(request):
    return render(request, 'contact.html')





def event_booking_list(request):
    events = Event.objects.all()
    
    # Iterate over each event and fetch the 3 most recent bookings
    for event in events:
        event.recent_bookings = Booking.objects.filter(event=event).order_by('-booked_on')[:3]
    
    # Pass events (with their recent bookings) to the template
    return render(request, 'event_booking_list.html', {'events': events})




@login_required
def feedback_view(request):
    form = FeedbackForm(request.POST or None)
    feedbacks = Feedback.objects.all().order_by('-id')

    if request.method == 'POST' and form.is_valid():
        feedback = form.save(commit=False)
        feedback.user = request.user
        feedback.save()
        return redirect('feedback')

    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})


@login_required
def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    form = FeedbackForm(request.POST or None, instance=feedback)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('feedback')
    return render(request, 'update_feedback.html', {'form': form})

@login_required
def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)

    if feedback.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this feedback.")

    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback')

    return render(request, 'delete_feedback.html', {'feedback': feedback})


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Here you can add the logic to store emails or integrate with newsletter services
        return HttpResponse("Thank you for subscribing!")
    return render(request, 'your_template.html')


@login_required(login_url='login')
def booking_view(request):
    all_events = Event.objects.all()
    selected_event = None
    event_id = request.GET.get('event_id')

    if event_id:
        selected_event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event_name = request.POST.get('eventname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_price = request.POST.get('payment_price')
        payment_description = request.POST.get('payment_description')
        payment_method = request.POST.get('payment_method')

        event_obj = get_object_or_404(Event, name=event_name)

        booking = Booking.objects.create(
            event=event_obj,
            name=name,
            email=email,
            phone=phone,
            payment_price=payment_price or event_obj.price,
            payment_description=payment_description,
            payment_method=payment_method,
        )

        booking.payment_status = True
        booking.save()

        try:
            send_mail(
                subject=f'Booking Confirmation for {event_name}',
                message=(
                    f'Hello {name},\n\nYour booking for "{event_name}" is confirmed. '
                    f'Thank you for your payment of {booking.payment_price}.\n\n— Eventify Team'
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, "🎉 Booking confirmed. Confirmation sent to your email.")
        except Exception as e:
            messages.error(request, f"Email failed to send: {e}")

        return redirect('event_booking_list')

    return render(request, 'booking.html', {
        'all_events': all_events,
        'selected_event': selected_event,
    })


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})


def booking_confirmation(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_confirmation.html', {'booking': booking})


def about(request):
    contact_info = {
        'name': 'Eventify',
        'email': 'eventify@gmail.com',
        'phone': '+91-734-567-7900',
    }

    company_info = {
        'name': 'Eventify Solutions',
        'description': 'We organize premium events including parties, functions, and corporate gatherings.',
        'address': '123, Eventify House, Pune, India',
        'founded_Year': 2025,
        'mission': 'To create unforgettable experiences for our clients. We strive to bring every event to life with creativity, precision, and passion. By understanding our clients unique needs, we deliver personalized and impactful moments that exceed expectations.',
        'vision': 'To be the leading event management company in the world. We aim to set the standard for innovation and excellence in event planning. Through continuous growth and commitment to quality, we aspire to inspire and transform the global event landscape.',
    }

    team = TeamMember.objects.all()

    return render(request, 'about.html', {
        'admin_details': contact_info,
        'company_info': company_info,
        'team': team
    })
