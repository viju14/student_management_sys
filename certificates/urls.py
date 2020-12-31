from rest_framework import routers
from django.urls import path,include
from certificates.views import CertificateView
router = routers.DefaultRouter()
router.register('api/v1', CertificateView,basename='My_srtf_api')# it provide list view and details
# router.register('api/v2', CustomUserProfileView,basename='MyAPIV1')

urlpatterns = [
    path('' ,include(router.urls))

]
