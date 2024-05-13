from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DrinkViewSet

router = DefaultRouter()
router.register(r'drinks', DrinkViewSet)

urlpatterns = [
  path('', include(router.urls)),
]

# urlpatterns = router.urls