from django.db import models

#if You want to add more Models means tables in SQL, you can add here

# Create your models here.

class TodoTable(models.Model):
    Date = models.CharField(max_length=100)
    Task = models.CharField(max_length=100)

    def __str__(self):
        return self.Task
