"""
URLs for hyperpay.
"""
from django.urls import re_path

from . import views

app_name = 'hyperpay'

urlpatterns = [
    # The processor slug in the path tells the status check which HyperPay entity created the checkout.
    re_path(r'^(?P<processor>[\w-]+)/return/$', views.HyperPayReturnView.as_view(), name='processor-return'),
    re_path(r'^(?P<processor>[\w-]+)/status/$', views.HyperPayStatusView.as_view(), name='processor-status'),
    # Slug-less routes: kept for checkouts created before the slugged routes existed (card processor).
    re_path(r'^return/$', views.HyperPayReturnView.as_view(), name='return'),
    re_path(r'^status/$', views.HyperPayStatusView.as_view(), name='status'),
]
