from django.contrib.auth.models import Group
from django.contrib import admin

from auth.models import User, Feature, Progress, UserAdmin, FeatureAdmin

# Remove default groups
admin.site.unregister(Group)

# Add our user to admin panel
admin.site.register(User, UserAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.register(Progress)
