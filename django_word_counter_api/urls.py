from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.cache import cache_page


app_name = 'api'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('v1/', include('api.urls'), name='homepage')
    url('', RedirectView.as_view(pattern_name='homepage', permanent=False)),
]