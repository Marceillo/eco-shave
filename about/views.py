from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm, FAQForm
from .models import FAQ
from django.urls import reverse


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
            # print(form.cleaned_data)
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

def faq(request):
    """
    View for the FAQ page
    """
    faqs = FAQ.objects.all()
    return render(request, 'about/faq.html', {'faqs': faqs})

@login_required
def add_faq(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can add another FAQ.')
        return redirect(reverse('faq'))

    if request.method == 'POST':
        form = FAQForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ has been added successfully!')
            return redirect('faq')
        else:
            messages.error(request, 'Failed to add to the FAQ.')
    else:
        form = FAQForm()
    
    return render(request, 'about/add_faq.html', {'form': form})

@login_required
def edit_faq(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can edit this FAQ.')
        return redirect(reverse('faq'))

    faq = get_object_or_404(FAQ, pk=pk)
    
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ  has been updated successfully!')
            return redirect('faq')
        else:
            messages.error(request, 'Failed to update the FAQ.')
    
    form = FAQForm(instance=faq)
    return render(request, 'about/edit_faq.html', {'form': form})


@login_required
def delete_faq(request, pk):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can delete this FAQ.')
        return redirect(reverse('faq'))
    faq = get_object_or_404(FAQ, pk=pk)
    
    if request.method == 'POST':
        faq.delete()
        messages.success(request, 'FAQ has been deleted successfully!')
        return redirect('faq')

    return render(request, 'about/faq_confirm_delete.html', {'faq': faq})

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'about/faq.html', {'faqs': faqs})