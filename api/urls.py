from rest_framework.routers import DefaultRouter
from api.views import BookingViewset

router = DefaultRouter()
router.register(r'booking', BookingViewset, 'booking')

urlpatterns = router.urls
