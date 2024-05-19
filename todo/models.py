from django.db import models

class Todo(models.Model):
    titel = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.titel

