from django.db import models
import uuid

# Create your models here.
class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=False, default="")
    author = models.CharField(max_length=200, blank=False, default="")
    headline = models.TextField(blank=False, default="")
    description = models.TextField(blank=False, default="")
    date_created = models.TextField(blank=False, default="")

def __str__(self):
    return self.title