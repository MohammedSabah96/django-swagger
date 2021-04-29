from rest_framework.routers import DefaultRouter
from .views import UserAccountView

router = DefaultRouter()
router.register("users", UserAccountView, basename="users_view")


urlpatterns = router.urls
