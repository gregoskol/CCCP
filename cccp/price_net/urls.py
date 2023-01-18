from django.urls import path

from . import views

app_name = "price_net"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.calc_create, name="calc_create"),
    path("calcs/<int:calc_id>/", views.calc_detail, name="calc_detail"),
    path("calcs/<int:calc_id>/edit/", views.calc_edit, name="calc_edit"),
    path(
        "calcs/<int:calc_id>/delete/confirm/",
        views.calc_delete_confirm,
        name="calc_delete_confirm",
    ),
    path(
        "calcs/<int:calc_id>/delete/",
        views.calc_delete,
        name="calc_delete",
    ),
    path(
        "change_prices/<int:rope_id>",
        views.change_prices,
        name="change_prices",
    ),
    path("prices_detail/", views.prices_detail, name="prices_detail"),
]
