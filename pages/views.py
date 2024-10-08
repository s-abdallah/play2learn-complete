from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/index.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
