from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',
           {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)
  return render(request,
          'listings/band_detail.html',
          {'band': band})

def about(request):
    return render(request, 'listings/about-us.html')

def listings(request):
	title = Listing.objects.all()
	return render(request, 'listings/listings.html',
		{'titles': title})

def contact(request):
	if request.method == 'POST':
		# créer une instance de notre formulaire et le remplir avec les données POST
		form = ContactUsForm(request.POST)

		if form.is_valid():
			send_mail(
				subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
				message=form.cleaned_data['message'],
				from_email=form.cleaned_data['email'],
				recipient_list=['admin@merchex.xyz'],
			)
		return redirect('email-sent')  # ajoutez cette instruction de retour
	else:
		# ceci doit être une requête GET, donc créer un formulaire vide
		form = ContactUsForm()
	return render(request,
		'listings/contact-us.html',
		{'form': form})
# Create your views here.
