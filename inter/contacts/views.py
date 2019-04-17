from django.shortcuts import render, redirect
from .models import Contact
import json

from django.contrib import messages

# Create your views here.
# view for homepage
def indexHome(request):
    return render(request, 'contacts/index.html', {
    })
# view for contacts lists
def indexContacts(request):
    context = {

    }
    all_contacts = Contact.objects.all()

    context['contacts'] = all_contacts
    return render(request, 'contacts/contacts.html', context)

# view for adding contacts
def createContacts(request):
    context = {

    }

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        # objects to record errors
        errors = {}

        # check for form errors
        if not name:
            errors['name'] = 'name field is required'

        if not email:
            errors['email'] = 'email is required'

        if not errors:
            print('yes')
            # find if mail exists
            try:
                Contact.objects.get(email=email)
                # send an error message because mail already exists
                errors['email'] = 'email already exists'
            except Contact.DoesNotExist:
                # email does not exits
                # save to that database
                new_contact = Contact(name=name, email=email)
                new_contact.save()

                messages.success(request, 'Your details has been saved')
                return redirect('/contacts')

        print(errors)


        messages.error(request, json.dumps(errors))    
    return render(request, 'contacts/create.html')

