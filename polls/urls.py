from django.conf.urls import url

from . import views

urlpatterns = [
    url('contact', views.ContactFormView.as_view(), name='contact'),
    url('success', views.success_view, name='success'),

]