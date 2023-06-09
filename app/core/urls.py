from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("", EventList.as_view(), name="events"),
    path("packs/", EmotionPackList.as_view(), name="packs_list"),
    path("packs_detail/<int:pk>/", EmotionPackDetail.as_view(), name="pack_detail"),
    path("events/<uuid:pk>/", EventDetail.as_view(), name="event_detail"),
    path("events/create/", EventCreate.as_view(), name="event_create"),
    path("vote/<uuid:pk>/", EventVote.as_view(), name="event_vote")

]

if 1 ==1 :
    pass
    """
    path("packs/<int:pk>/", ProductsListView.as_view(), name="products_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/", OrderDetailsView.as_view(), name="order_details"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    """
