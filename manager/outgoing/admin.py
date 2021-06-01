from django.contrib import admin

from outgoing.models import Outgoing


class OutgoingAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date_creation', 'date_update', 'publications',)
    list_display_links = ('id', 'number',)
    search_fields = ('number',)
    list_filter = ('fixed',)
    list_editable = ('publications',)
    fields = (
        'id', 'number', 'company', 'fixed', 'document', 'date_creation', 'date_update', 'comment', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    filter_horizontal = ('company', 'fixed',)
    save_on_top = True


admin.site.register(Outgoing, OutgoingAdmin)
