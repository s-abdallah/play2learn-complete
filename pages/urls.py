from django.urls import path

from .views import HomePageView, AboutPageView, ContactPageView, ContactSuccessView

app_name = "pages"
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about/", AboutPageView.as_view(), name="aboutpage"),
    path("contact/", ContactPageView.as_view(), name="contactpage"),
    path("contact-success/", ContactSuccessView.as_view(), name="contact_success"),
]
