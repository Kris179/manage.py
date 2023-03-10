from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = {
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  path('', include('main.urls')),
                  path('catalogs/', include('catalogs.urls')),
              } + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

