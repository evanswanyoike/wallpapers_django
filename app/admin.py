from django.contrib import admin

# Register your models here.
from app.models import WallpaperImage, Category, SourceWebsite, ImageSizeAttribute


#
#
# class WallpaperImageAdmin(admin.StackedInline):
#     model = WallpaperImage
# classes = ['collapse']


# @admin.register(Wallpaper)
# class WallpaperAdmin(admin.ModelAdmin):
#     inlines = [WallpaperImageAdmin]
#     list_display = ("name", "id", "category", "date_modified")
#
#     class Meta:
#         model = Wallpaper


@admin.register(WallpaperImage)
class WallpaperImageAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "id", "category", "length", "width", "image_size_attribute", "color", "date_modified")
    pass


###

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "name", "id", "date_modified",)
    # list_filter = ("name", "id", "date_modified", "date_published",)
    search_fields = ("name", "id", "date_modified", "date_published",)


admin.site.register(Category, CategoryAdmin)


class SourceWebsiteAdmin(admin.ModelAdmin):
    list_display = ("name", "id",)
    list_filter = ("name", "id",)
    search_fields = ("name", "id",)


admin.site.register(SourceWebsite, SourceWebsiteAdmin)


class ImageSizeAttributeAdmin(admin.ModelAdmin):
    list_display = ("name", "id",)
    list_filter = ("name", "id",)
    search_fields = ("name", "id",)


admin.site.register(ImageSizeAttribute, ImageSizeAttributeAdmin)
