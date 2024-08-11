from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    plan_at = models.DateField(null=True, blank=True, db_index=True)
    priority = models.PositiveSmallIntegerField(default=100, db_index=True)

    def mark_as_completed(self):
        self.is_completed = True
        self.completed_at = timezone.now()
        self.save()

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.is_completed and not self.completed_at:
            self.completed_at = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title
