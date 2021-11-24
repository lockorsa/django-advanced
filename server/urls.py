"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path
from health_check import urls as health_urls

from server.apps.adminapp import urls as adminapp_urls
from server.apps.authapp import urls as authapp_urls
from server.apps.basket import urls as basket_urls
from server.apps.geekshop import urls as geekshop_urls
from server.apps.index import urls as index_urls
from server.apps.news import urls as news_urls

admin.autodiscover()

urlpatterns = [
    # Apps:
    path('admin/', include(adminapp_urls, namespace='adminapp')),
    path('', include(authapp_urls, namespace='authapp')),
    path('basket/', include(basket_urls, namespace='basket')),
    path('', include(geekshop_urls, namespace='geekshop')),
    path('', include(index_urls, namespace='index')),
    path('news/', include(news_urls, namespace='news')),

    # Health checks:
    path('health/', include(health_urls)),  # noqa: DJ05

    # django-admin:
    path('admin_legacy/doc/', include(admindocs_urls)),  # noqa: DJ05
    path('admin_legacy/', admin.site.urls),

    # It is a good practice to have explicit index view:
    # BUT I DONT FOLLOW IT :)
    # path('', index, name='index'),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),  # noqa: DJ05
    ] + urlpatterns + static(  # type: ignore
        # Serving media files in development only:
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
