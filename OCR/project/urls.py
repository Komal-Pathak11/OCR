from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^tresult/(?P<dest>[-\w\+]+)/(?P<text>[-\w\+]+)/$', views.translate, name='translate'),
    url(r'^translated/$', views.translated, name='translated'),

]