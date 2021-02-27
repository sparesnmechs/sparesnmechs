"""UserProfiles app admin."""
from django.contrib import admin

import snm.userprofiles.models as models

admin.site.register(models.UserProfile)
