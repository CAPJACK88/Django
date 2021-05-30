from django.contrib import admin
from score.models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date_creation', 'date_update', 'publications',)
    filter_horizontal = ('company', 'fixed', 'contract')
    list_display_links = ('id', 'number',)
    search_fields = ('number',)
    list_editable = ('publications',)
    fields = ('id', 'number', 'company', 'fixed', 'contract', 'date_creation', 'date_update', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    save_on_top = True


admin.site.register(Score, ScoreAdmin)
