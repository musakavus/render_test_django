import logging

from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        logging.error('Form validation failed in home view.')
        form = ContactForm()

    return render(request, 'home1.html', {'form': form})
