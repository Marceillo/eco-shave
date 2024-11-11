from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def about(request):
    """
    Returns the about page and
    display relevant information.
    """

    return render(request, 'about/about.html')


def contact(request):
    """
    Allows a user to get in touch with the blog.
    Using a form the user send a message with their details.
    about/contact template used.
    """
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            messages.success(
                request,
                'Your message has been received successfully!')

            return redirect('contact_success')
        else:
            messages.error(request, 'Error submitting your message.')
            form = ContactForm()

    return render(request, 'about/contact.html', {'form': form})


def contact_success(request):
    """
    A success message after form submitted.
    """
    return render(request, 'about/contact_success.html')
