from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Dailybook(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    emotion_choices = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('neutral', 'Neutral'),
    ]
    emotion = models.CharField(max_length=10, choices=emotion_choices)
    date_edit = models.DateTimeField()

    def __str__(self):
        return self.title

