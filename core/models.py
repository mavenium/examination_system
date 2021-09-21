from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from extensions import choices


class Course(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
        null=False,
        unique=True,
        blank=False
    )
    content = RichTextUploadingField(
        verbose_name=_('Content'),
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
