from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import get_user_model, Feature, Progress
from authentication.admin import models

# Remove default groups
admin.site.unregister(Group)

# Add our user to admin panel
admin.site.register(get_user_model(), models.UserAdmin)
admin.site.register(Feature)
admin.site.register(Progress)
