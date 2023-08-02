from django.db import models
from commons.models import CommonModel
from items.models import Item


class ItemStatsDaily(CommonModel):

    """Item analysis per day"""

    total_daily_items = models.IntegerField()
    nego_selected_items = models.IntegerField()
    avg_selected_days_to_sell = (
        models.IntegerField()
    )  # average 'sold_days' of items posted on today (need to calculate accuately when you merge the average of 'this average')


class SearchCategory(models.Model):
    category = models.CharField(max_length=25, choices=Item.CategoryChoices.choices)

    def __str__(self):
        return self.category


class SearchLocation(models.Model):
    location = models.CharField(max_length=10, choices=Item.LocationChoices.choices)

    def __str__(self):
        return self.location


class SearchUsedYears(models.Model):
    used_years = models.CharField(max_length=20, choices=Item.UsedYearChoices.choices)

    def __str__(self):
        return self.used_years


class SearchStats(CommonModel):

    """Item Search Statistic Model Definition"""

    user_id = models.TextField(default="")
    searched_categories = models.ManyToManyField(SearchCategory, blank=True)
    searched_locations = models.ManyToManyField(SearchLocation, blank=True)
    searched_used_years = models.ManyToManyField(SearchUsedYears, blank=True)
    most_searched_keyword = models.CharField(max_length=255, null=True, blank=True)

    # def __str__(self):
    #     return f"{self.created_at}: {', '.join(str(category) for category in self.searched_categories.all())}, {', '.join(str(location) for location in self.searched_locations.all())}, {', '.join(str(used_years) for used_years in self.searched_used_years.all())}, {self.most_searched_keyword}"
