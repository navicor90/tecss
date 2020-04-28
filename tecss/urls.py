from django.conf.urls import url

from . import views
from .ListViews import CustomerListView


urlpatterns = [ 
        url(r'^$', views.index, name='index'),
        url(r'^receipt_from_order$', views.receipt_from_order, name='receipt_from_order'),
        url(r'^customers$', CustomerListView.as_view(), name='customers'),
        url(r'^new_customer$', views.new_customer, name='new_customer'),
        url(r'^(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
        url(r'^(?P<pk>\d+)/items/$', views.customer_items, name='customer_items'),
        ]
