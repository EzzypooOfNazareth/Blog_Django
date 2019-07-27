from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from databse.models import BlogPost

from .views import (
    home_page,
    posts_page,
    post_view
)

urlpatterns = [
    path('', home_page),
    path('posts/', posts_page),
    path('posts/<int:id>', post_view),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
