from django.urls import path

from .views import (
    CustomPasswordChangeView,
    MyAccountPageView,
    SubmitReviewView,
    ReviewDetailView,
    ReviewDeleteView,
    ReviewUpdateView,
    ReviewListView,
    TrackingListView,
)

urlpatterns = [
    path(
        "password/change/",
        CustomPasswordChangeView.as_view(),
        name="account_change_password",
    ),
    path("my-account/", MyAccountPageView.as_view(), name="my-account"),
    path("review/<slug>/update/", ReviewUpdateView.as_view(), name="update-review"),
    path("review/<slug>/delete/", ReviewDeleteView.as_view(), name="delete-review"),
    path("add-review/", SubmitReviewView.as_view(), name="add-review"),
    path("review/<slug>/", ReviewDetailView.as_view(), name="read-review"),
    path("my-reviews/", ReviewListView.as_view(), name="list-review"),
    path("my-tracking/", TrackingListView.as_view(), name="list-tracking"),
]
