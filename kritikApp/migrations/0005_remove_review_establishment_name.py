# Generated by Django 5.0.2 on 2024-03-14 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kritikApp', '0004_remove_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='establishment_name',
        ),
    ]