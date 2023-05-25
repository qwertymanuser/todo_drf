from rest_framework.routers import DefaultRouter

from apps.todo.views import ToDoAPIViewSet

router = DefaultRouter()
router.register('todo', ToDoAPIViewSet, 'api_todo')

urlpatterns = router.urls