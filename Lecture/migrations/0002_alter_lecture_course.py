# Generated by Django 3.2.6 on 2021-12-19 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_initial'),
        ('Lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='Course.course', verbose_name='Курсс'),
        ),
    ]
