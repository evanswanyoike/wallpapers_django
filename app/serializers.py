from rest_framework import serializers

from app.models import WallpaperImage, Category, ImageSizeAttribute


# class WallpaperSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wallpaper
#         fields = ("name", "date_modified", "date_published", "category", "author", "sourceURL", "images",)
#         depth = 1

class CatSER(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class WallpaperImageSerializer(serializers.ModelSerializer):
    category = CatSER()

    class Meta:
        model = WallpaperImage
        fields = "__all__"
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ImageSizeAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSizeAttribute
        fields = "__all__"
