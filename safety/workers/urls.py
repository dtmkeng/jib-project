from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import (
    WorkerListView,
    # WorkerListViewSetView,
)
# router = DefaultRouter()
# router.register(r'', WorkerListViewSetView)
urlpatterns = [
    path('', WorkerListView.as_view()),
    # path('', include(router.urls)),
]
