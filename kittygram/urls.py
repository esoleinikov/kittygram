from django.urls import path, include

from cats.views import CatList, CatDetail, CatViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
