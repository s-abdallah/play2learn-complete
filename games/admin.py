from django.contrib import admin
from .models import GameTracking


# Register your models here.
@admin.register(GameTracking)
class GameTrackAdmin(admin.ModelAdmin):
    model = GameTracking
    list_display = [
        "game_type",
        "user",
        "game_settings",
        "score",
        "tries",
        "start_time",
        "end_time",
    ]

    # Customizing List View
    # List Attributes
    date_hierarchy = "updated"
    list_filter = ["updated", "score", "tries"]
    ordering = ["-updated"]
    search_fields = ["score", "tries"]

    # Form attributes
    autocomplete_fields = ["user"]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ("created", "updated")
        return ()
