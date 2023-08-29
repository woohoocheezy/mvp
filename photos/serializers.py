from rest_framework.serializers import ModelSerializer
from .models import Photo


class PhotoSerializer(ModelSerializer):

    """Serializer Definition for Photo"""

    class Meta:
        model = Photo

        fields = (
            "pk",
            "file",  # cloudflare로부터 받은 URL
        )

    # def to_representation(self, instance):
    #     """Return the first photo instead of all photos"""
    #     first_photo = instance.item.photos.first()
    #     if first_photo:
    #         return {"pk": first_photo.pk, "file": first_photo.file}
    #     else:
    #         return None
