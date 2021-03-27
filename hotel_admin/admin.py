from django.contrib import admin

from .models import *


admin.site.register(Table, admin.ModelAdmin)
admin.site.register(Room, admin.ModelAdmin)
admin.site.register(Dish, admin.ModelAdmin)

