from django.conf.urls import url

from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<person_id>[0-9]+)/$', views.person_detail, name= 'person_detail'),
    url(r'^(?P<person_id>[0-9]+)/update/$', views.update, name= 'update')
    ]