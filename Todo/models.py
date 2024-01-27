from django.db import models


from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title