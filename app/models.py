from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.utils.html import format_html


class Category(models.Model):
    name = models.CharField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    background = models.ImageField(upload_to="images/category_bg/", null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="70px" />' % self.background.url)

    image_tag.short_description = "Image"


class SourceWebsite(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Source Website'
        verbose_name_plural = "Source Websites"

    def __str__(self):
        return f"{self.name}"


class ImageSizeAttribute(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Image Size Attribute'
        verbose_name_plural = "Images Sizes Attributes"

    def __str__(self):
        return f"{self.name}"


# class Wallpaper(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     date_modified = models.DateTimeField(auto_now=True)
#     date_published = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     sourceURL = models.URLField(null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Wallpaper'
#         verbose_name_plural = "Wallpapers"
#
#     def __str__(self):
#         return f"{self.name}"


class WallpaperImage(models.Model):
    # wallpaper = models.ForeignKey(Wallpaper, default=None, null=True, blank=True, on_delete=models.SET_NULL,
    #                               related_name='images')
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sourceURL = models.URLField(null=True, blank=True)
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    image_size_attribute = models.ForeignKey(ImageSizeAttribute, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images')
    color = ColorField(format="hexa", image_field='image')

    # color = ColorField(image_field='image')

    class Meta:
        verbose_name = 'Wallpaper'
        verbose_name_plural = "Wallpapers"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="70px" />' % self.image.url)

    image_tag.short_description = "Image"

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>', self.color
        )
