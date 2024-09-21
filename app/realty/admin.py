from django.contrib import admin

from realty.servises import get_floor_by_flat
from .models import Flat, Floor

admin.AdminSite.site_header = "Администрирование сайта недвижимости"
admin.AdminSite.site_title = "Администрирование"
admin.AdminSite.index_title = "Сайт недвижимости"


class FlatAdmin(admin.ModelAdmin):
    fields = [
        "number",
        "area",
        "rooms_count",
        "floor",
        "status",
        "created_at",
    ]

    readonly_fields = ["created_at"]
    list_display = [
        "number",
        get_floor_by_flat,
        "rooms_count",
        "area",
        "wc_count",
        "status",
        "created_at",
    ]
    list_filter = ["rooms_count", "status"]


class FloorAdmin(admin.ModelAdmin):
    fields = ["floor", "flats_count", "status", "description", "created_at"]
    readonly_fields = ["created_at"]
    list_display = [
        "floor",
        "flats_count",
        "status",
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Floor, FloorAdmin)
