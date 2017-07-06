from django.db import models

# Create your models here.
class Entry(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """A string representation of the model."""
        return self.text[:50]
