from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from album.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Albums,name="album"),
] + static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
