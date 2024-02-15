from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing


def hello(request):
	bands = Band.objects.all()
	return render(request, 'listings/hello.html',
        {'bands': bands})

def about(request):
    return render(request, 'listings/about-us.html')

def listings(request):
	title = Listing.objects.all()
	return render(request, 'listings/listings.html',
		{'titles': title})

def contact(request):
    return render(request, 'listings/contact-us.html')

# Create your views here.
