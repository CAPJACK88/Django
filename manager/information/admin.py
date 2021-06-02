from django.contrib import admin
from information.models import Information, CategoryInformation


class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_creation', 'date_update', 'publications',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'text',)
    list_filter = ('category',)
    list_editable = ('publications',)
    fields = (
        'id', 'title', 'text', 'category', 'fixed', 'document', 'document_01', 'document_02', 'date_creation', 'date_update',
        'comment', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    filter_horizontal = ('fixed', 'category',)
    save_on_top = True


class CategoryInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True


admin.site.register(Information, InformationAdmin)
admin.site.register(CategoryInformation, CategoryInformationAdmin)
