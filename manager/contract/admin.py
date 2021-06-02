from django.contrib import admin
from contract.models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'company_02', 'date_creation', 'date_update', 'submitted', 'publications', )
    filter_horizontal = ('company', 'fixed', 'score',)
    list_display_links = ('id', 'number',)
    search_fields = ('number',)
    list_editable = ('submitted', 'publications',)
    fields = ('id', 'number', 'company', 'company_02', 'fixed', 'date_creation', 'date_update', 'publications',)
    readonly_fields = ('id', 'date_creation', 'date_update',)
    save_on_top = True


admin.site.register(Contract, ContractAdmin)
