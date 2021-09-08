from rest_framework.routers import DefaultRouter

from .views import FleetViewSet

router = DefaultRouter()
router.register(
    prefix="fleets",
    viewset=FleetViewSet,
    basename="fleets",
)

urlpatterns = router.urls
