from django.db import models
from django.contrib.auth.models import User
from users.models import Manager, Executor

class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    deadline = models.DateTimeField(verbose_name='Deadline', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    manager = models.ForeignKey(Manager, related_name='managed_tasks', on_delete=models.CASCADE)
    executors = models.ManyToManyField(Executor, related_name='executed_tasks')
    
    class Meta:
        verbose_name ='Task'
        verbose_name_plural = 'Tasks'
    
    def __str__ (self):
        return self.name