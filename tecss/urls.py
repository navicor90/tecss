from django.conf.urls import url

from . import views
from .ListViews import CustomerListView


urlpatterns = [ 
        url(r'^$', views.index, name='index'),
        url(r'^customers$', CustomerListView.as_view(), name='customers'),
        url(r'^new_customer$', views.newCustomer, name='new_customer'),
        url(r'^(?P<pk>\d+)/$', views.customerDetail, name='customer_detail'),
        url(r'^(?P<pk>\d+)/items/$', views.customerItems, name='customer_items'),
        ]
