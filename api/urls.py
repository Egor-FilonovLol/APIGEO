from django.contrib import admin
from django.urls import path, include
from .views import LocationCreateView, MessageLocationView, SearchPoint, MessageRadius
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('points/', LocationCreateView.as_view()),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('points/<int:location_id>/messages/', MessageLocationView.as_view()),
        path('points/search/', SearchPoint.as_view()),
        path('messages/search/', MessageRadius.as_view()),
    ])),
]
