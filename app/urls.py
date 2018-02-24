from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from . import apis

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^api/login/$', apis.user_login, name='api_login'),
    url(r'^api/logout/$', apis.user_logout, name='api_logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)