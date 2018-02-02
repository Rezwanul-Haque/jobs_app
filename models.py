from django.db import models

# Create your models here.
class JobListening(models.Model):
    # TODO: Define fields here
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
