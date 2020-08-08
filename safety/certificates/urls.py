from django.urls import include, re_path
from .views import CertificateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CertificateView)

urlpatterns = [
   re_path('', include(router.urls)),
]
