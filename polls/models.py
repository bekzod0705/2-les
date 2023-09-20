from django.db import models
from datetime import datetime
# Create your models here.
class TodoModel(models.Model):
    name=models.CharField(max_length=70,default='')
    date=models.DateTimeField(default=datetime.now)
    description=models.TextField()
    status=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name