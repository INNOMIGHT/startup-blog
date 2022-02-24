from rest_framework.routers import SimpleRouter
from .viewsets import TagViewSet, StartupViewSet


api_router = SimpleRouter()

api_router.register("tag", TagViewSet, basename='tag-api')
api_router.register("startup", StartupViewSet, basename='startup-api')

api_routes = api_router.urls

urlpatterns = api_routes + []