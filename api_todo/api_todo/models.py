from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    