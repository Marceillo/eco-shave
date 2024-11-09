from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.contrib import messages


def about(request):
    """
    Returns the about page and
    display relevant information.
    """

    return render(request, 'about/about.html')



