from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maincat.urls', namespace='home')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('merch/', include('merch.urls', namespace='merch')),
    path('collection/', include('collection.urls', namespace='collection')),
    path('', include('users.urls', namespace='users')),



]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


