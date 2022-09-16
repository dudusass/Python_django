from rest_framework import routers
from django.urls import path, include

from taskboard.views import BoardViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
