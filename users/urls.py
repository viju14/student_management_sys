from rest_framework import routers
from users.views import CustomUserViewSet, CustomUserProfileView
router = routers.SimpleRouter()
router.register('api/v1', CustomUserViewSet,basename='Myuserapi')# it provide list view and details
# router.register('api/v2', CustomUserProfileView,basename='MyAPIV1')

urlpatterns = router.urls



