# Generated by Django 3.2.6 on 2021-12-17 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachcour',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studcour',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course'),
        ),
        migrations.AddField(
            model_name='studcour',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_user', to=settings.AUTH_USER_MODEL, verbose_name='автор курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(related_name='student_user', through='Course.StudCour', to=settings.AUTH_USER_MODEL, verbose_name='студент курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher_user', through='Course.TeachCour', to=settings.AUTH_USER_MODEL, verbose_name='соавтор курса'),
        ),
    ]