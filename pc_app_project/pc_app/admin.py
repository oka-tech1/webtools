from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.profile)
admin.site.register(models.pc_store)
admin.site.register(models.contact)
admin.site.register(models.wallet)
