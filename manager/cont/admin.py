from django.contrib import admin
from .models import Contact, Company
from django.utils.safestring import mark_safe


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'surname', 'email', 'telephone', 'mobile_phone', 'date_update', 'publications', 'get_photo',)
    list_display_links = ('id', 'name', 'surname',)
    search_fields = ('name', 'surname',)
    list_filter = ('company', 'position')
    list_editable = ('publications',)
    fields = ('id', 'name', 'surname', 'middle_name', 'email', 'telephone', 'mobile_phone', 'url', 'date_birth',
              'photo', 'get_photo', 'date_creation', 'date_update', 'comment', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update', 'get_photo',)
    filter_horizontal = ('company', 'position',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Нет фото'

    get_photo.short_description = 'Миниатюра'


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inn', 'kpp', 'telephone', 'publications',)
    list_display_links = ('id', 'name', 'inn',)
    search_fields = ('name', 'inn', 'kpp', 'address', 'telephone', 'fixed',)
    list_filter = ('fixed',)
    list_editable = ('publications',)
    fields = ('id', 'name', 'inn', 'kpp', 'address', 'telephone', 'url', 'photo', 'card', 'fixed', 'date_creation',
              'date_update', 'comment', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    filter_horizontal = ('fixed',)
    save_on_top = True


admin.site.register(Contact, ContactAdmin)
admin.site.register(Company, CompanyAdmin)
