from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # добавьте это поле
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Dailybook(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # добавьте это поле
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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)


    def __str__(self):
        return f"Profile for {self.user}"