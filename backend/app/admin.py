from django.contrib import admin

from .models import Poll, Option, Question


class PollAdmin(admin.ModelAdmin):
    ...

class OptionAdmin(admin.ModelAdmin):
    ...

class QuestionAdmin(admin.ModelAdmin):
    ...

admin.site.register(Poll, PollAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Question, QuestionAdmin)
