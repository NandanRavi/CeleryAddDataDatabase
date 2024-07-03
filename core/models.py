from django.db import models
from datetime import datetime
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    publisher_name = models.CharField(max_length=30)
    rating = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(null=True, blank=True)


    # class Meta:
    #     ordering = ['-created']