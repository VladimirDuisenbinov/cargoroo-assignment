from rest_framework.routers import DefaultRouter

from .views import BikeViewSet

router = DefaultRouter()
router.register(
    prefix="bikes",
    viewset=BikeViewSet,
    basename="bikes",
)

urlpatterns = router.urls
