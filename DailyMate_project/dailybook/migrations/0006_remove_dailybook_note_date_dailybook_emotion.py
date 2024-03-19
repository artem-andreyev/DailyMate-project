# Generated by Django 4.2.5 on 2024-03-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailybook', '0005_rename_date_created_dailybook_note_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailybook',
            name='note_date',
        ),
        migrations.AddField(
            model_name='dailybook',
            name='emotion',
            field=models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('angry', 'Angry'), ('neutral', 'Neutral')], default='happy', max_length=10),
            preserve_default=False,
        ),
    ]