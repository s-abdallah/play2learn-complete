from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ["name", "email", "subject", "submitted_at"]
    search_fields = ("name", "email", "subject")

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ("created", "updated")
        return ()
