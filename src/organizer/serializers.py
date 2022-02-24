from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, ModelSerializer
from .models import Startup, Tag


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "tag-api-detail"
            }
        }


class StartupSerializer(HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "startup-api-detail"
            }
        }