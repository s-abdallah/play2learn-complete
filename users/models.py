from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.utils.text import slugify
import hashlib

from django.db import models

from django.urls import reverse

from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError("Avatar must be no bigger than 200x200 pixels.")


class CustomUser(AbstractUser):
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)

    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        help_text="Image must be 200px by 200px.",
        validators=[validate_avatar],
    )

    def get_absolute_url(self):
        return reverse("my-account")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Review(models.Model):
    class Meta:
        ordering = ["review"]

    review = models.TextField()
    slug = models.SlugField(max_length=300, unique=True, null=False, editable=False)
    # add User field to the model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("read-review", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            # Use the first 10 characters of the review to generate the slug
            review_snippet = self.review[:50]  # Extract first 50 characters
            base_slug = slugify(review_snippet)  # Slugify the snippet
            unique_slug = f"{base_slug}-{hashlib.md5(self.user.username.encode('utf-8')).hexdigest()[:6]}"  # Ensure uniqueness using hash
            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review by {self.user.username}"
