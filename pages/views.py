from django.urls import reverse_lazy

from django.views.generic import FormView, CreateView, TemplateView
from django.core.mail import send_mail
from django.conf import settings

# from common.utils.email import send_email
from common.utils.local_email import send_email

from .forms import ContactForm
from .models import Contact


# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/index.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ContactPageView(CreateView):
    model = Contact
    # template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("pages:contact_success")

    def form_valid(self, form):
        contact = form.save()
        data = form.cleaned_data

        # Send email to the admin
        subject = f"New Contact Us Form Submission from {contact.name}"
        message = f"Subject: {contact.subject}\n\nMessage:\n{contact.message}\n\nFrom: {contact.name} ({contact.email})"
        send_email(settings.ADMIN_EMAIL, subject, message)

        return super().form_valid(form)

    # def get_object(self):
    #     return self.request.contact


class ContactSuccessView(TemplateView):
    template_name = "pages/contact_success.html"
