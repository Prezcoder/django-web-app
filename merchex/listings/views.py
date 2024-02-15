from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing


def hello(request):
	bands = Band.objects.all()
	title = Listing.objects.all()
	return render(request, 'listings/hello.html',
        {'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1>')

def contact(request):
    return HttpResponse('<h1>Contact us</h1> <p>On veut vous entendre !</p>')

# Create your views here.
