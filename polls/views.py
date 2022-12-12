# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, FormView, ListView
from .models import Contacts
from .forms import ContactsForm
from .tasks import test
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class ContactFormView(FormView):
    model = Contacts
    form_class = ContactsForm
    success_url = '/contact'
    template_name = 'contact.html'

    def form_valid(self, form):

        # form.save()
        # # write_file.delay(form.instance.email)
        test.delay()
        return super().form_valid(form)

def success_view(request):
    print('RECIPIENTS_EMAIL')
    return HttpResponse('Приняли! Спасибо за вашу заявку.')