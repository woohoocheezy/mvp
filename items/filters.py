from django.db.models import Q
from django_filters import rest_framework as filters
from .models import FixedPriceItem


class ItemFilter(filters.FilterSet):
    category = filters.ChoiceFilter(choices=FixedPriceItem.CategoryChoices.choices)
    # used_years = filters.ChoiceFilter(choices=FixedPriceItem.UsedYearChoices.choices)
    price = filters.RangeFilter()
    location = filters.ChoiceFilter(choices=FixedPriceItem.LocationChoices.choices)
    search = filters.CharFilter(method="search_item")

    class Meta:
        model = FixedPriceItem
        fields = ["category", "price", "location", "search"]


def search_item(self, queryset, name, value):
    return queryset.filter(
        Q(item_name__icontains=value) | Q(item_description__icontains=value)
    )
