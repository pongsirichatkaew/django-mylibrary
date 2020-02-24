from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Listing


def index(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(
                description__icontains=keywords) | Q(title__icontains=keywords)
                                                 | Q(company__icontains=keywords)
                                                 | Q(author__name__icontains=keywords))
    context = {'listings': queryset_list}
    return render(request, 'listings/search.html', context)
