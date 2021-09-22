from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from extensions import choices

from ckeditor_uploader.fields import RichTextUploadingField


class Course(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
        null=False,
        unique=True,
        blank=False
    )
    description = models.TextField(
        verbose_name=_('Description'),
        null=False,
        blank=False
    )
    content = RichTextUploadingField(
        verbose_name=_('Content'),
        null=False,
        blank=False
    )
    exam = models.ForeignKey(
        'Exam',
        verbose_name=_('Exam'),
        on_delete=models.PROTECT,
        related_name='course_exam',
        null=False,
        blank=False
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )
    last_update_time = models.DateTimeField(
        verbose_name=_('Last Update Time'),
        auto_now=True,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = _("Courses")
        verbose_name = _("Course")
        ordering = ['-pk']


class Question(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
        null=False,
        unique=True,
        blank=False
    )
    correct_answer = models.PositiveSmallIntegerField(
        verbose_name=_('Correct Answer'),
        choices=choices.FourOptions.choices,
        null=False,
        blank=False
    )
    choice_one = models.ForeignKey(
        'Choice',
        verbose_name=_('Choice One'),
        on_delete=models.PROTECT,
        related_name='question_choice_one',
        null=False,
        blank=False
    )
    choice_two = models.ForeignKey(
        'Choice',
        verbose_name=_('Choice Two'),
        on_delete=models.PROTECT,
        related_name='question_choice_two',
        null=False,
        blank=False
    )
    choice_three = models.ForeignKey(
        'Choice',
        verbose_name=_('Choice Three'),
        on_delete=models.PROTECT,
        related_name='question_choice_three',
        null=False,
        blank=False
    )
    choice_four = models.ForeignKey(
        'Choice',
        verbose_name=_('Choice Four'),
        on_delete=models.PROTECT,
        related_name='question_choice_four',
        null=False,
        blank=False
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )
    last_update_time = models.DateTimeField(
        verbose_name=_('Last Update Time'),
        auto_now=True,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = _("Questions")
        verbose_name = _("Question")
        ordering = ['-pk']


class Choice(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
        null=False,
        unique=True,
        blank=False
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )
    last_update_time = models.DateTimeField(
        verbose_name=_('Last Update Time'),
        auto_now=True,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = _("Choices")
        verbose_name = _("Choice")
        ordering = ['-pk']


class Exam(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
        null=False,
        unique=True,
        blank=False
    )
    questions = models.ManyToManyField(
        Question,
        verbose_name=_("Questions"),
        related_name='exam_questions'
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )
    last_update_time = models.DateTimeField(
        verbose_name=_('Last Update Time'),
        auto_now=True,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = _("Exams")
        verbose_name = _("Exam")
        ordering = ['-pk']


class ExamResult(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.PROTECT,
        related_name='result_exam_user',
        null=False,
        blank=False
    )
    exam = models.ForeignKey(
        'Exam',
        verbose_name=_('Exam'),
        on_delete=models.PROTECT,
        related_name='result_exam_exam',
        null=False,
        blank=False
    )
    course = models.ForeignKey(
        'Course',
        verbose_name=_('Course'),
        on_delete=models.PROTECT,
        related_name='result_exam_exam',
        null=False,
        blank=False
    )
    result = models.JSONField(
        verbose_name=_('Result'),
        null=False,
        blank=False
    )
    wrong_count = models.PositiveSmallIntegerField(
        verbose_name=_('Wrong Count'),
        default=0,
        null=False,
        blank=False
    )
    correct_count = models.PositiveSmallIntegerField(
        verbose_name=_('Correct Count'),
        default=0,
        null=False,
        blank=False
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return f'Course : {self.course} - Exam : {self.exam}'

    class Meta:
        verbose_name_plural = _("Exam Results")
        verbose_name = _("Exam Result")
        ordering = ['-pk']
