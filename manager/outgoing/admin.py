from django.contrib import admin

from outgoing.models import Outgoing, CategoryOutgoing


class OutgoingAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'company_02', 'date_creation', 'date_update', 'publications',)
    list_display_links = ('id', 'number',)
    search_fields = ('number',)
    list_filter = ('fixed',)
    list_editable = ('publications',)
    fields = (
        'id', 'number', 'company', 'company_02', 'fixed', 'CategoryOutgoing', 'document', 'date_creation', 'date_update', 'comment',
        'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    filter_horizontal = ('company', 'fixed', 'CategoryOutgoing',)
    save_on_top = True


class CategoryOutgoingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True


admin.site.register(Outgoing, OutgoingAdmin)
admin.site.register(CategoryOutgoing, CategoryOutgoingAdmin)
