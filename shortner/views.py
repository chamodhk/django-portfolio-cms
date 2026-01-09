from django.shortcuts import render

# Create your views here.

from django.db.models import F
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from .models import ShortURL


def follow_short_url(request, code):
    short_url = get_object_or_404(ShortURL, code=code)

    if not short_url.is_active:
        raise Http404("This short URL is inactive.")

    ShortURL.objects.filter(pk=short_url.pk).update(
        click_count=F("click_count") + 1
    )

    return redirect(short_url.destination_url)