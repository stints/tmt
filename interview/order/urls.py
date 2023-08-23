from rest_framework.routers import DefaultRouter

from interview.order.views import OrderListCreateView, OrderTagListCreateView

router = DefaultRouter()
router.register(r"tags", OrderTagListCreateView)
router.register(r"", OrderListCreateView)

urlpatterns = router.urls
