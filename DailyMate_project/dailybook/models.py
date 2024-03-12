from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Dailybook(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    note_date = models.DateTimeField()

    def __str__(self):
        return self.title
