from rest_framework.routers import DefaultRouter
from .views import TodoView


router = DefaultRouter()
router.register("todos", TodoView, basename="todos_view")

urlpatterns = router.urls
