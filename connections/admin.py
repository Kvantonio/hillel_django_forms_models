from django.contrib import admin

from .models import Author_quote, Quote


class Author_quoteAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote']
    search_fields = ['quote']
    fields = ['quote']


admin.site.register(Author_quote, Author_quoteAdmin)
admin.site.register(Quote, QuoteAdmin)
