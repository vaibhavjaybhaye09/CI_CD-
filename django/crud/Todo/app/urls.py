from .views import TodoVIewset
from rest_framework.router import DfaultRouter


router = DefaultRouter()
router.register('api/todo', TodoVIewset, basename= 'todo')

urlpatterns = router.urls