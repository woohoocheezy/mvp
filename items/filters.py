from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Item


class ItemFilter(filters.FilterSet):
    category = filters.ChoiceFilter(choices=Item.CategoryChoices.choices)
    used_years = filters.ChoiceFilter(choices=Item.UsedYearChoices.choices)
    price = filters.RangeFilter()
    location = filters.ChoiceFilter(choices=Item.LocationChoices.choices)
    search = filters.CharFilter(method="search_item")

    class Meta:
        model = Item
        fields = ["category", "used_years", "price", "location", "search"]


def search_item(self, queryset, name, value):
    return queryset.filter(
        Q(item_name__icontains=value) | Q(item_description__icontains=value)
    )
