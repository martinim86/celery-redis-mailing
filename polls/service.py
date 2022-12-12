from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Contacts
from django.template.loader import  render_to_string
def send():
    list = []
    contacts = Contacts.objects.all()
    for contact in contacts:
        data = {
            "name": contact.name,
            "surname": contact.last_name,
            "date_birth": contact.date_of_birth,
            "msg": "We invite you to our meeting",
            "email": contact.email,
        }
        html_content = render_to_string('template_send.html', data)
        msg = EmailMultiAlternatives(contact.name, 'Here is the message.', 'from@example.com', [contact.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()



