from django.contrib import admin
from .models import User, Position
from django.utils.safestring import mark_safe


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'get_photo',)
    list_display_links = ('id', 'surname',)
    search_fields = ('name', 'surname',)
    fields = ('id', 'name', 'surname', 'description', 'get_photo', 'photo',)
    filter_horizontal = ('position',)
    readonly_fields = ('id', 'get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Нет фото'

    get_photo.short_description = 'Миниатюра'


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'description',)
    list_display_links = ('id', 'position',)
    search_fields = ('position',)
    fields = ('id', 'position', 'description',)
    readonly_fields = ('id',)
    save_on_top = True


admin.site.register(User, UserAdmin)
admin.site.register(Position, PositionAdmin)
