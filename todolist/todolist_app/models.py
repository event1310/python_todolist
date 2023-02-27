from django.db import models
import uuid
class Todo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    def __str__(self):
        return self.title



class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )

    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name