from django.urls import path
from . import views


urlpatterns = [
    # path('', views.WallpaperListAPIView.as_view(), name="wallpapers"),
    path('', views.WallpaperImageListAPIView.as_view(), name="all"),
    path('category', views.CategoryListAPIView.as_view(), name="category"),
    path('sizes', views.ImageSizeAttributeListAPIView.as_view(), name="sizes"),
]
