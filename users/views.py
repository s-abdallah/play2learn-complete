from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from allauth.account.views import PasswordChangeView

from .models import Review
from .forms import CustomUserChangeForm, ReviewForm

# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("my-account")


class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = "account/my_account.html"

    success_message = "Update Successful"

    def get_object(self):
        return self.request.user


class SubmitReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm

    # add success message Mixin
    success_message = "Review submitted."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewListView(ListView):
    model = Review
    paginate_by = 5


class ReviewDetailView(DetailView):
    model = Review


class ReviewUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Review

    form_class = ReviewForm
    # add success message Mixin
    success_message = "Review updated."

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy("list-review")

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

    def form_valid(self, form):
        messages.success(self.request, "Review deleted.")
        return super().form_valid(form)
