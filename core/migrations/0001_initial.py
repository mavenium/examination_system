# Generated by Django 3.2.7 on 2021-09-17 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Title')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='Last Update Time')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Title')),
                ('correct_answer', models.PositiveSmallIntegerField(choices=[(None, '---------'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')], verbose_name='Correct Answer')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='Last Update Time')),
                ('choice_four', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_choice_four', to='core.choice', verbose_name='Choice Four')),
                ('choice_one', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_choice_one', to='core.choice', verbose_name='Choice One')),
                ('choice_three', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_choice_three', to='core.choice', verbose_name='Choice Three')),
                ('choice_two', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_choice_two', to='core.choice', verbose_name='Choice Two')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Title')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='Last Update Time')),
                ('questions', models.ManyToManyField(related_name='exam_questions', to='core.Question', verbose_name='Questions')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
                'ordering': ['-pk'],
            },
        ),
    ]
