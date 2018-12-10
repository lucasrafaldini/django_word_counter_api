from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic.base import RedirectView

app_name = 'api'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('v1/', include('api.urls')),
    url('', RedirectView.as_view(pattern_name='homepage', permanent=False)),
]