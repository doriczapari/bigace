from django.contrib import admin
from .models import UserProfile, Project, Task, Technology

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Technology)

# Register your models here.
