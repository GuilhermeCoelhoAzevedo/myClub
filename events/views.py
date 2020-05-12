from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import VenueForm
from .models import Venue, Event

def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)

    #Verify next calendar - Pagination
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    # Verify previous calendar - Pagination
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year

    if year < 2000 or year > 2099:
        year = date.today().year

    cal = HTMLCalendar().formatmonth(year, month)

    if year == date.today().year and month == date.today().month:
        cal = cal.replace('>%i<' % date.today().day, ' bgcolor="#228B22"><b><u>%i</u></b><' % date.today().day)

    events = Event.objects.filter(event_date__year=year, event_date__month=month)

    context = {
        'month_name': calendar.month_name[month],
        'cal': cal,
        'year': year,
        'next_month': next_month,
        'next_year': next_year,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'events': events
    }

    return render(request, 'events/calendar_base.html', context)

def add_venue(request):
    submitted = False

    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
    }

    return render(request, 'events/add_venue.html', context)

def about(request):
    return render(request, 'events/about.html')