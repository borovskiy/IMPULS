from rest_framework import routers
from .views import BookingViewSet
router = routers.SimpleRouter()
router.register('booking', BookingViewSet)

urlpatterns = []
urlpatterns += router.urls