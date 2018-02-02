from django.contrib import admin
from .models import JobListening
# Register your models here.

class JobListeningAdmin(admin.ModelAdmin):
    """Django admin ModelAdmin for data model JobListening"""
    list_display = ["title", "description"]



admin.site.register(JobListening, JobListeningAdmin)
