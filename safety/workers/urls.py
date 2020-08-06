from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  (
    WorkerListView,
    WorkerListViewSetView,
)
router = DefaultRouter()
router.register(r'', WorkerListViewSetView)
urlpatterns = [
    path('xxx', WorkerListView.as_view()),
    path('', include(router.urls)),
]
