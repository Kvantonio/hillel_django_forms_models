from django.contrib import admin

from .models import Choice, Logs, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class LogModelAdmin(admin.ModelAdmin):
    list_display = ("path", "method", 'timestamp')
    fields = ['path', 'method']
    list_filter = ["method"]
    search_fields = ['method', 'path', "timestamp"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Logs, LogModelAdmin)
