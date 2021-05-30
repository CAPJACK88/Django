from django.contrib import admin
from contract.models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date_creation', 'date_update', 'publications',)
    filter_horizontal = ('company', 'fixed', 'score',)
    list_display_links = ('id', 'number',)
    search_fields = ('number',)
    list_editable = ('publications',)
    fields = ('id', 'number', 'company', 'fixed', 'date_creation', 'date_update', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    save_on_top = True


admin.site.register(Contract, ContractAdmin)
