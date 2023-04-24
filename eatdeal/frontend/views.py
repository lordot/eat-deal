from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PromoRequestForm


def index(request):
    context = {
        'GOOGLE_API': settings.GOOGLE_API,
        'DEFAULT_CITY': settings.DEFAULT_CITY
    }
    return render(request, 'index.html', context)


@login_required
def promo_request(request):
    if request.method == 'POST':
        form = PromoRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PromoRequestForm()
    return render(request, 'request.html', {'form': form})
