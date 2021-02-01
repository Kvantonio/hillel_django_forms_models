from django.contrib import admin

from .models import Creator, Quote


class CreatorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote']
    search_fields = ['quote']
    fields = ['quote']


admin.site.register(Creator, CreatorAdmin)
admin.site.register(Quote, QuoteAdmin)
