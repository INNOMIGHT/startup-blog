from tracemalloc import start
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import TagSerializer, StartupSerializer
from .models import Tag, Startup
from rest_framework.decorators import action
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_204_NO_CONTENT
from django.shortcuts import get_object_or_404


class TagViewSet(ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class StartupViewSet(ModelViewSet):

    serializer_class = StartupSerializer
    queryset = Startup.objects.all()
    lookup_field = "slug"


    @action(detail=True, methods=["HEAD", "GET", "POST"], url_path="tags")
    def tags(self, request, slug=None):
        # relate a Posted Tag
        startup = self.get_object()
        print(startup)
        if request.method in ("HEAD", "GET"):
            s_tag = TagSerializer(
                startup.tags,
                many=True,
                context={"request": request}
            )
            return Response(s_tag.data)

        tag_slug = request.data.get("slug")

        if not tag_slug:
            return Response(
                "Slug of Tag must be specified",
                status=HTTP_400_BAD_REQUEST
            )
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        startup.tags.add(tag)
        startup.save()
        return Response(HTTP_204_NO_CONTENT)