from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "상품 사진"
        verbose_name_plural = "상품 사진들"
