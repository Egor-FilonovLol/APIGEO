
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as dock
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += dock
