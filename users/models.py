from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_manager = models.BooleanField(default=False, verbose_name='Manager')
    is_executor = models.BooleanField(default=False, verbose_name='Executor')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.is_manager:
            manager, created = Manager.objects.get_or_create(user=self)
            manager.save()

        if self.is_executor:
            executor, created = Executor.objects.get_or_create(user=self)
            executor.save()

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Executor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username