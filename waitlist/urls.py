from rest_framework import routers
from django.urls import path,include
from waitlist.views import WaitlistViewset
router = routers.DefaultRouter()
router.register('api/v1', WaitlistViewset,basename='Myuserapi')# it provide list view and details
# router.register('api/v2', CustomUserProfileView,basename='MyAPIV1')

urlpatterns = [
    path('' ,include(router.urls))

]