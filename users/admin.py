from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

from common.admin import DjangoGamesAdmin

CustomUser = get_user_model()
from .models import Review


@admin.register(CustomUser)
class CustomUserAdmin(DjangoGamesAdmin, UserAdmin):
    model = CustomUser

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Optional Fields",
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name"),
            },
        ),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ["review", "user", "is_featured", "created", "updated"]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ("slug", "created", "updated")

        return ()


admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
