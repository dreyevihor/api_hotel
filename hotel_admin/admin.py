from django.contrib import admin

from .models import *


class DishOrderInline(admin.TabularInline):
    model = DishOrder


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        DishOrderInline
    ]


admin.site.register(Table, admin.ModelAdmin)
admin.site.register(Room, admin.ModelAdmin)
admin.site.register(Dish, admin.ModelAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(RoomService, admin.ModelAdmin)
admin.site.register(TableBooking, admin.ModelAdmin)
admin.site.register(News, admin.ModelAdmin)

