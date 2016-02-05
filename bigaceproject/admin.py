from django.contrib import admin
from .models import UserProfile, Project, Task, Technology, Rating

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Technology)
admin.site.register(Rating)

# Register your models here.
