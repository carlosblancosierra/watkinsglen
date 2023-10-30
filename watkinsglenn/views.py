from django.shortcuts import render, redirect
from django.contrib import messages

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


def home_page(request):
    context = {}

    return render(request, "home.html", context)
