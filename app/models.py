

from django.db import models


# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=20,blank=False)
    description=models.CharField(max_length=20,blank=False)
    date=models.DateField(auto_now_add=True)
    is_completed=models.BooleanField(default=True)
    class meta:
        db_table='todo'

    def __str__(self):
        return self.title
        