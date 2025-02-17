# diagrams/models.py
from django.db import models
from django.contrib.postgres.fields import JSONField  # For PostgreSQL
# If you're not on Postgres, you can use django-jsonfield or a similar package.

class Diagram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    data = models.JSONField()  # Stores shapes, positions, connections, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
