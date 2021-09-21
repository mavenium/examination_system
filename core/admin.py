from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core import models


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'create_time',
        'last_update_time',
    ]
    list_display_links = [
        'title'
    ]
    list_filter = [
        'create_time',
        'last_update_time',
    ]
    search_fields = [
        'title',
    ]
    actions = [
        'delete_selected',
    ]
    ordering = [
        '-create_time'
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related()


class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'create_time',
        'last_update_time',
    ]
    list_display_links = [
        'title'
    ]
    list_filter = [
        'create_time',
        'last_update_time',
    ]
    search_fields = [
        'title',
    ]
    actions = [
        'delete_selected',
    ]
    ordering = [
        '-create_time'
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related()


class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'correct_answer',
        'create_time',
        'last_update_time',
    ]
    list_display_links = [
        'title'
    ]
    list_filter = [
        'create_time',
        'last_update_time',
    ]
    search_fields = [
        'title',
    ]
    actions = [
        'delete_selected',
    ]
    ordering = [
        '-create_time'
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related()


class ExamAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'create_time',
        'last_update_time',
    ]
    list_display_links = [
        'title'
    ]
    list_filter = [
        'create_time',
        'last_update_time',
    ]
    search_fields = [
        'title',
    ]
    actions = [
        'delete_selected',
    ]
    ordering = [
        '-create_time'
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related()


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Exam, ExamAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
admin.site.register(models.Question, QuestionAdmin)
