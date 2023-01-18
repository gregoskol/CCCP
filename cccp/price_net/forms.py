from django import forms

from .models import CalcPrice, Rope


class CalcForm(forms.ModelForm):
    class Meta:
        model = CalcPrice
        fields = (
            "name_of_rope",
            "client",
            "date_of_check",
            "number_of_check",
            "rope_lenght",
            "rope_width",
            "rope_cell",
            "margin",
            "margin",
            "longitud",
            "across",
            "liktros",
            "thimble_amount",
            "thimble_price_one",
            "clamp_amount",
            "clamp_price_one",
            "nor_amount",
            "nor_price_one",
            "crossing",
            "braid_thimble",
            "braid_thimble_amount",
            "splice",
            "braid_oogen",
            "discount",
            "deadline",
            "comment",
        )


class RopeForm(forms.ModelForm):
    class Meta:
        model = Rope
        fields = (
            "price",
            "price_thimble",
            "price_oogen",
            "price_crossing",
            "price_splice",
        )
