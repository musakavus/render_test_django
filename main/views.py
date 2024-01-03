from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully.')
            return redirect('home')

    else:
        form = ContactForm()

    return render(request, 'home1.html', {'form': form})
