from django.contrib import admin
from .models import Question, Answer
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'max_choice', 'date')
    list_filter = ('date',)
    search_fields = ('title',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)