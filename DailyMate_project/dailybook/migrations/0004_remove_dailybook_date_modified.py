# Generated by Django 4.2.5 on 2024-03-12 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailybook', '0003_dailybook_remove_entry_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailybook',
            name='date_modified',
        ),
    ]