from django.conf import settings
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=200, verbose_name="Title")
    memo = models.TextField(max_length=255, blank=True,
                            null=True, verbose_name="Memo")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
