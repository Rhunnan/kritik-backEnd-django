# Generated by Django 5.0.2 on 2024-03-14 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kritikApp', '0003_remove_establishment_reviews_remove_user_bookmarks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
    ]