# Generated by Django 5.0.2 on 2024-03-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kritikApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='ai_script',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
