from django.contrib import admin
from users.models import Manager, Executor, User
from .models import Task


# class AuthorAdmin(admin.ModelAdmin):
#     pass
admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Executor)
admin.site.register(Task)