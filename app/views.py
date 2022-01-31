from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response

from .serializers import WallpaperImageSerializer, CategorySerializer, \
    ImageSizeAttributeSerializer
from .models import Category, SourceWebsite, ImageSizeAttribute, WallpaperImage
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import renderers, filters
from app.renderers import CustomRenderer


# class WallpaperListAPIView(ListAPIView):
#     serializer_class = WallpaperSerializer
#     queryset = Wallpaper.objects.all()
#     # renderer_classes = [renderers.JSONRenderer]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filter_fields = ['date_published', 'category', 'name']
#     search_fields = ['date_published', 'category', 'name']
#     ordering_fields = '__all__'


class WallpaperImageListAPIView(ListAPIView):
    serializer_class = WallpaperImageSerializer
    queryset = WallpaperImage.objects.all()
    # renderer_classes = [renderers.JSONRenderer]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['color', 'length', 'width', "image_size_attribute"]
    search_fields = ['color', 'length', 'width', "image_size_attribute__name", "category__name"]
    ordering_fields = '__all__'
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    # def get(self, request):
    #     serializer = WallpaperImageSerializer()
    #     return Response(serializer.data, status=200)


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # renderer_classes = [renderers.JSONRenderer]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['name', "date_modified", "date_published", ]
    search_fields = ['name', "date_modified", "date_published", ]
    ordering_fields = '__all__'
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]



class ImageSizeAttributeListAPIView(ListAPIView):
    serializer_class = ImageSizeAttributeSerializer
    queryset = ImageSizeAttribute.objects.all()
    # renderer_classes = [renderers.JSONRenderer]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['name', "id"]
    search_fields = ['name', "id"]
    ordering_fields = '__all__'
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

