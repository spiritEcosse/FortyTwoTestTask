from django.conf.urls import patterns, include, url
from fortytwo_test_task.views import IndexView
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
