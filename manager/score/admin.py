from django.contrib import admin
from score.models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'company_02', 'date_creation', 'date_update', 'publications', 'payment', 'production',)
    filter_horizontal = ('company', 'fixed', 'contract')
    list_display_links = ('id', 'number',)
    search_fields = ('number',)
    list_editable = ('publications', 'payment', 'production',)
    fields = ('id', 'number', 'company', 'company_02', 'fixed', 'contract', 'date_creation', 'date_update', 'payment', 'production',
              'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    save_on_top = True


admin.site.register(Score, ScoreAdmin)
