from django.contrib import admin
from django.contrib.auth.models import Group

# from authentication.models import Feature, Progress
from authentication.models import UserRepository

# Remove default groups
admin.site.unregister(Group)

# Add our user to admin panel
admin.site.register(UserRepository.model, UserRepository.admin)
# admin.site.register(Feature)
# admin.site.register(Progress)
