from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from . import settings
from .yasg import urlpatterns as doc_urls
from allauth.account.views import confirm_email


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
