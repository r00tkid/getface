from django.contrib import admin
from django.contrib.auth.models import Group

from authentication.models import User, Feature, Progress

# Remove default groups
admin.site.unregister(Group)

# Add our user to admin panel
admin.site.register(User.model(), User.admin_view())
admin.site.register(Feature.model(), Feature.admin_view())
admin.register(Progress.model())
