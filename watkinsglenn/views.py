from django.shortcuts import render, redirect
from django.contrib import messages

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from homesites.models import Homesite


def home_page(request):
    qs = Homesite.objects.filter(hidden=False)

    context = {
        "homesites": qs,
    }

    return render(request, "home.html", context)
