from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.contrib import messages


def about(request):
    """
    Returns the about page and
    display relevant information.
    """

    return render(request, 'about/about.html')


# def contact(request):
#     """
#     Allows a user to get in touch with the blog.
#     Using a form the user send a message with their details.
#     about/contact template used.
#     """
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request,
#                 'Your message has been received successfully!')

#             return redirect('about')
#         else:
#             messages.error(request, 'Error submitting your message.')
#             form = ContactForm()

#     return render(request, 'about/contact.html', {'form': form})


# def contact_success(request):
#     return render(request, 'about/contact_success.html')
