from django.contrib import admin
from core.models import Settings,  Data


# Register your models here.
admin.site.register(Data)
admin.site.register(Settings)