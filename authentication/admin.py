from django.contrib.auth.models import Group
from django.contrib import admin

from authentication.models import User, Feature, Progress

# Remove default groups
admin.site.unregister(Group)

# Add our user to admin panel
admin.site.register(User.model, User.admin)
admin.site.register(Feature.model, Feature.admin)
admin.register(Progress.model)
