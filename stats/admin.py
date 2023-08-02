from django.contrib import admin
from .models import (
    ItemStatsDaily,
    SearchStats,
    SearchCategory,
    SearchLocation,
    SearchUsedYears,
)


@admin.register(ItemStatsDaily)
class ItemStatsDailyAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "total_daily_items",
        "nego_selected_items",
        "avg_selected_days_to_sell",
    )
    list_filter = ("created_at",)
    search_fields = (
        "total_daily_items",
        "nego_selected_items",
        "avg_selected_days_to_sell",
    )


# @admin.register(SearchCategory)
# class SearchCategoryAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "category",
#     )


# @admin.register(SearchLocation)
# class SearchLocationAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "location",
#     )


# @admin.register(SearchUsedYears)
# class SearchUsedYearsAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "used_years",
#     )


@admin.register(SearchStats)
class SearchStatsDailyAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "user_id",
        "get_searched_categories",
        "get_searched_locations",
        "get_searched_used_years",
        "most_searched_keyword",
    )
    list_filter = ("created_at",)
    search_fields = ("user_id", "most_searched_keyword")

    def get_searched_categories(self, obj):
        return ", ".join(
            [category.category for category in obj.searched_categories.all()]
        )

    get_searched_categories.short_description = "Searched Categories"

    def get_searched_locations(self, obj):
        return ", ".join(
            [location.location for location in obj.searched_locations.all()]
        )

    get_searched_locations.short_description = "Searched Locations"

    def get_searched_used_years(self, obj):
        return ", ".join(
            [used_years.used_years for used_years in obj.searched_used_years.all()]
        )

    get_searched_used_years.short_description = "Searched Used Years"
