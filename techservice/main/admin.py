from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Car)
admin.site.register(TypeMaintenance)
admin.site.register(RecordMaintenance)
admin.site.register(Notification)
