from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from .models import Document, Category


class DocumentAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Document
        fields = '__all__'


class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_update', 'document', 'publications', 'category',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'description',)
    list_filter = ('category',)
    list_editable = ('publications',)
    fields = (
        'title', 'description', 'document', 'category', 'date_creation', 'date_update', 'surname', 'publications',)
    readonly_fields = ('date_creation', 'date_update',)
    save_on_top = True
    form = DocumentAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True


admin.site.register(Document, DocAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Уапавление документами'
admin.site.site_header = 'Уапавление документами'
