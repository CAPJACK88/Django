from django.contrib import admin
from .models import Document, Category


class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_update', 'document', 'publications',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'description',)
    list_filter = ('category',)
    list_editable = ('publications',)
    fields = ('id', 'title', 'document', 'category', 'username', 'date_creation', 'date_update', 'description',
              'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    filter_horizontal = ('username',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True


admin.site.register(Document, DocAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Панель управления'
admin.site.site_header = 'Панель управления'
