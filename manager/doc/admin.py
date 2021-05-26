from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Document, Category, User


class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_update', 'document', 'publications', 'category',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'description',)
    list_filter = ('category',)
    list_editable = ('publications',)
    fields = ('title', 'description', 'document', 'category', 'date_creation', 'date_update', 'username', 'publications',)
    readonly_fields = ('date_creation', 'date_update', 'username',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'description', 'get_photo',)
    list_display_links = ('id', 'username',)
    search_fields = ('username',)
    fields = ('id', 'username', 'description', 'get_photo', 'photo',)
    readonly_fields = ('id', 'get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Нет фото'
    get_photo.short_description = 'Миниатюра'


admin.site.register(Document, DocAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_title = 'Уапавление документами'
admin.site.site_header = 'Уапавление документами'
