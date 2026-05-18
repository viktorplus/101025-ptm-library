from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    library = models.ForeignKey(
        'Library',
        on_delete=models.CASCADE,
        related_name='events'
    )
    books = models.ManyToManyField(
        'Book',
        related_name='events'
    )


class EventParticipant(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    member = models.ManyToManyField(
        'User',
        related_name='events'
    )
    registration_date = models.DateTimeField(default=timezone.now)

def __str__(self):
    user_list = [user.username for user in self.member.all()]
    return f"EventParticipant: {user_list} - {self.registration_date}"