from django.contrib import admin

from search.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    save_on_top = True


admin.site.register(City, CityAdmin)
