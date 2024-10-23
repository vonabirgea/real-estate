from django.contrib import admin
from .models import Flat, Floor, Entrance, Building, Project

admin.AdminSite.site_header = "Администрирование сайта недвижимости"
admin.AdminSite.site_title = "Администрирование"
admin.AdminSite.index_title = "Сайт недвижимости"


class FlatAdmin(admin.ModelAdmin):
    def get_floor_by_flat(self, flat):
        return flat.floor.floor

    get_floor_by_flat.short_description = "Этаж"

    fields = [
        "number",
        "area",
        "rooms_count",
        "floor",
        "status",
        "created_at",
    ]

    readonly_fields = ["floor", "created_at"]

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
    def get_entrance_by_floor(self, floor):
        return floor.entrance.number

    get_entrance_by_floor.short_description = "Номер подъезда"

    fields = ["floor", "flats_count", "status", "description", "created_at"]
    readonly_fields = ["created_at"]
    list_display = [
        "floor",
        "flats_count",
        "status",
        "get_entrance_by_floor",
    ]
    list_select_related = ["entrance"]


class EntranceAdmin(admin.ModelAdmin):
    def get_building_by_entrance(self, entrance):
        return entrance.building.number

    get_building_by_entrance.short_description = "Номер дома"

    def get_project_by_entrance(self, entrance):
        return entrance.building.project.name

    get_project_by_entrance.short_description = "Проект"

    fields = ["number", "flats_count", "floors_count"]
    readonly_fields = ["created_at"]
    list_display = [
        "number",
        "flats_count",
        "floors_count",
        "get_building_by_entrance",
        "get_project_by_entrance",
    ]
    list_select_related = ["building__project"]


class BuildingAdmin(admin.ModelAdmin):
    def get_project_by_building(self, building):
        return building.project.name

    get_project_by_building.short_description = "Проект"

    fields = ["number", "entrances_count", "project"]
    readonly_fields = ["created_at", "project"]
    list_display = ["number", "entrances_count", "get_project_by_building"]
    list_select_related = ["project"]


class ProjectAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "buildings_count",
        "description",
        "created_at",
        "last_update",
    ]
    readonly_fields = ["created_at", "last_update", "buildings_count"]
    list_display = ["name", "buildings_count", "description"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Entrance, EntranceAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Project, ProjectAdmin)
