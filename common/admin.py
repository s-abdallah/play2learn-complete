from django.contrib import admin

# Register your models here.
admin.site.index_title = "Home"
admin.site.site_title = "Django Play2Learn Admin"
admin.site.site_header = "Django Play2Learn Admin"


class DjangoGamesAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 1000
