from django.db import models
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')

    def __str__(self):
        return self.title

    def mark_as_completed(self):
        self.completed = True
        self.save()

    def is_overdue(self):
        if self.due_date and timezone.now() > self.due_date:
            return True
        return False

    class Meta:
        ordering = ['due_date', 'priority']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
