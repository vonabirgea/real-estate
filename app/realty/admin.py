from django.contrib import admin
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

    def get_floor_by_flat(self, flat):
        return flat.floor.floor

    get_floor_by_flat.short_description = "Этаж"

    list_display = [
        "number",
        "get_floor_by_flat",
        "rooms_count",
        "area",
        "wc_count",
        "status",
        "created_at",
    ]
    list_select_related = ["floor"]
    list_filter = ["rooms_count", "status"]


class FloorAdmin(admin.ModelAdmin):
    fields = ["floor", "flats_on_floor", "status", "description", "created_at"]
    readonly_fields = ["created_at"]
    list_display = [
        "floor",
        "flats_on_floor",
        "status",
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Floor, FloorAdmin)
