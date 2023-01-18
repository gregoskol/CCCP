from django.contrib import admin

from .models import CalcPrice, Rope


class RopeAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "price",
        "price_thimble",
        "price_oogen",
        "price_crossing",
        "price_splice",
    )
    # list_editable = ("owner", "account")
    search_fields = ("type",)
    # list_filter = ("date_of_buy",)
    empty_value_display = "-не задана-"


class CalcPriceAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name_of_rope",
        "number_of_check",
        "date_of_check",
        "client",
        "rope_lenght",
        "rope_width",
        "rope_cell",
        "margin",
        "longitud",
        "longitud_lenght",
        "longitud_amount",
        "longitud_price_one",
        "longitud_price_total",
        "across",
        "across_lenght",
        "across_amount",
        "across_price_one",
        "across_price_total",
        "liktros",
        "liktros_lenght",
        "liktros_amount",
        "liktros_price_one",
        "liktros_price_total",
        "thimble_amount",
        "thimble_price_one",
        "thimble_price_total",
        "clamp_price_one",
        "clamp_price_total",
        "nor_price_one",
        "nor_price_total",
        "crossing",
        "crossing_amount",
        "crossing_price_one",
        "crossing_price_total",
        "braid_thimble",
        "braid_thimble_amount",
        "braid_thimble_price_one",
        "braid_thimble_price_total",
        "splice",
        "splice_amount",
        "splice_price_one",
        "splice_price_total",
        "braid_oogen",
        "braid_oogen_amount",
        "braid_oogen_price_one",
        "braid_oogen_price_total",
        "discount",
        "deadline",
        "comment",
        "price_total",
    )
    # search_fields = ("type",)
    empty_value_display = "0"


admin.site.register(Rope, RopeAdmin)
admin.site.register(CalcPrice, CalcPriceAdmin)
