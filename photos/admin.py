from django.contrib import admin
from .models import Photo
from django.contrib.contenttypes.admin import GenericTabularInline


# @admin.register(Photo)
# class PhotoAdmin(admin.ModelAdmin):
#     # list_display = (
#     #     "file",
#     #     "item_id",
#     #     "item",
#     # )

#     class Meta:
#         #     "photo_uuid",
#         verbose_name = "상품 사진"
#         verbose_name_plural = "상품 사진들"


class PhotoInline(GenericTabularInline):
    model = Photo
    ct_field = "content_type"
    ct_fk_field = "object_id"
    extra = 1


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "photo_uuid",
        "file",
        "content_type",
        "object_id",
        "created_at",
        "updated_at",
    )
    search_fields = ("photo_uuid", "object_id")
    readonly_fields = ("photo_uuid", "created_at", "updated_at")
