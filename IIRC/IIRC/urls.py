"""IIRC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings

from django.conf.urls import url, include
from django.contrib import admin
from blogs import views
from arabicblog import views as ar_views
from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r"^blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    url(r"^ar/blog/", include("arabicblog.urls", namespace="arabicblog")),
    url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^$', views.homepage, name='homepage'),
    url(r'^lar/', views.arHome, name='arHome'),

    url(r'^en/', views.en, name='en'),
    url(r'^ar/', ar_views.ar, name='ar'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),

    url(r'^blogs/', include('blogs.urls')),
    url(r'^base/', views.index, name='index'),
    url(r'^test/', views.post, name='test'),
    url(r'^home/', views.home, name='home'),

    # url(r"^account/", include("account.urls")),
    # url(r"^comments/", include("pinax.comments.urls", namespace="pinax_comments")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
