from django.db import models


# Create your models here.
class Todo(models.Model):
    """Todoモデル"""

    title = models.CharField(max_length=255)
    memo = models.TextField(max_length=255)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    # user = models.ForeignKey()

    def __str__(self):
        return self.name