from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Contact


def index(request):
    """Old style view : just to show how it was done before
    """
    result = {}
    result["contacts"] = Contact.objects.all()
    return render(request, 'notebook/index.html', result)


class ContactListView(ListView):

    model = Contact
    context_object_name = "contacts"


class ContactDetailView(DetailView):

    model = Contact
    context_object_name = "contact"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all emails
        context['emails'] = self.object.email_set.all()
        return context


class ContactCreateView(CreateView):

    model = Contact
    fields = ["first_name", "last_name", "birthday"]


class ContactUpdateView(UpdateView):

    model = Contact
    fields = ["first_name", "last_name", "birthday"]
