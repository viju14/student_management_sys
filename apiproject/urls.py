
from django.contrib import admin
from django.urls import path,include
from users.views import CustomUserProfileView
from users.urls import router as ur
from certificates.urls import router as cr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/profile/', CustomUserProfileView.as_view(), name='user-profile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/',include('users.urls')),
    path('crtf/',include('certificates.urls')),
    path('lect/', include('lecture.urls')),


]
