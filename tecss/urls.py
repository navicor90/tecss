from django.conf.urls import url

from . import views


urlpatterns = [ 
        url(r'^$', views.customers, name='index'),
        url(r'^new_customer$', views.newCustomer, name='new Customer'),
        url(r'^(?P<pk>\d+)/$', views.customerDetail, name='Customer Detail'),
        url(r'^(?P<pk>\d+)/items/$', views.customerItems, name='Customer Items'),
        ]
