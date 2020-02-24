from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)
    context = {'listings': listings}
    return render(request, 'pages/index.html', context)
