import locale
import math

from django.core.paginator import Paginator
from django.db.models import Max
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from price_net.forms import CalcForm, RopeForm
from price_net.models import CalcPrice, Rope

NUMBERS_OF_LIMIT = 15


def paginator(request, calc_list):
    paginator = Paginator(calc_list, NUMBERS_OF_LIMIT)
    calc_number = request.GET.get("page")
    return paginator.get_page(calc_number)


def index(request):
    template = "index.html"
    calc_list = CalcPrice.objects.all()
    page_obj = paginator(request, calc_list)
    context = {
        "page_obj": page_obj,
    }
    return render(request, template, context)


def calc_create(request):
    template = "price_net/create_calc.html"
    ropes = CalcPrice.objects.aggregate(max_number=Max("number"))
    form = CalcForm(request.POST or None)
    form.fields["braid_thimble"].queryset = Rope.objects.exclude(
        price_thimble=None
    )
    form.fields["crossing"].queryset = Rope.objects.exclude(
        price_crossing=None
    )
    form.fields["splice"].queryset = Rope.objects.exclude(price_splice=None)
    form.fields["braid_oogen"].queryset = Rope.objects.exclude(
        price_oogen=None
    )
    if request.method == "POST":
        if form.is_valid():
            calc = form.save(commit=False)
            calc.number = ropes["max_number"] + 1
            calculate(calc)
            calc.save()
            return redirect(
                reverse("price_net:calc_detail", args=[calc.number])
            )
    return render(request, template, {"form": form})


def calc_detail(request, calc_id):
    template = "price_net/calc_detail.html"
    calc = get_object_or_404(CalcPrice, number=calc_id)
    form = CalcForm(request.POST or None)
    context = {
        "calc": calc,
        "form": form,
    }
    return render(request, template, context)


def calc_edit(request, calc_id):
    calc = get_object_or_404(CalcPrice, number=calc_id)
    template = "price_net/create_calc.html"
    form = CalcForm(request.POST or None, instance=calc)
    calc.rope_width = locale.str(calc.rope_width)
    calc.rope_lenght = locale.str(calc.rope_lenght)
    calc.margin = locale.str(calc.margin)
    if calc.date_of_check is not None:
        date = calc.date_of_check.strftime("%Y-%m-%d")
    else:
        date = 0
    if request.method == "POST":
        if form.is_valid():
            calc = form.save(commit=False)
            calculate(calc)
            form.save()
            return redirect(
                reverse("price_net:calc_detail", args=[calc.number])
            )
    return render(
        request,
        template,
        {"form": form, "calc": calc, "is_edit": True, "date": date},
    )


def calc_delete_confirm(request, calc_id):
    template = "price_net/delete_calc.html"
    return render(
        request,
        template,
        {
            "calc_id": calc_id,
        },
    )


def calc_delete(request, calc_id):
    CalcPrice.objects.filter(number=calc_id).delete()
    return redirect(reverse("price_net:index"))


def change_prices(request, rope_id):
    rope = get_object_or_404(Rope, id=rope_id)
    template = "price_net/change_prices.html"
    form = RopeForm(request.POST or None, instance=rope)
    if rope.price is not None:
        rope.price = locale.str(rope.price)
    if rope.price_thimble is not None:
        rope.price_thimble = locale.str(rope.price_thimble)
    if rope.price_oogen is not None:
        rope.price_oogen = locale.str(rope.price_oogen)
    if rope.price_crossing is not None:
        rope.price_crossing = locale.str(rope.price_crossing)
    if rope.price_splice is not None:
        rope.price_splice = locale.str(rope.price_splice)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("price_net:prices_detail"))
    return render(
        request,
        template,
        {"form": form, "rope": rope},
    )


def prices_detail(request):
    ropes = Rope.objects.all()
    template = "price_net/prices_detail.html"
    context = {
        "ropes": ropes,
    }
    return render(request, template, context)


def calculate(calc):
    calc.longitud_lenght = calc.rope_lenght + 0.5
    longitud_rope = get_object_or_404(Rope, type=calc.longitud)
    calc.longitud_amount = math.ceil(
        (calc.rope_lenght * 1000 / calc.rope_cell) - 1
    )
    calc.longitud_price_one = longitud_rope.price
    calc.longitud_price_total = (
        calc.margin
        * calc.longitud_lenght
        * calc.longitud_amount
        * calc.longitud_price_one
    )
    calc.across_lenght = calc.rope_width + 0.5
    across_rope = get_object_or_404(Rope, type=calc.across)
    calc.across_amount = math.ceil(
        (calc.rope_width * 1000 / calc.rope_cell) - 1
    )
    calc.across_price_one = across_rope.price
    calc.across_price_total = (
        calc.margin
        * calc.across_lenght
        * calc.across_amount
        * calc.across_price_one
    )
    calc.liktros_lenght = (calc.rope_lenght + calc.rope_width) * 2 + 5
    if calc.liktros is None:
        calc.liktros_price_one = 0
    else:
        liktros_rope = get_object_or_404(Rope, type=calc.liktros)
        calc.liktros_price_one = liktros_rope.price
    calc.liktros_amount = 1
    calc.liktros_price_total = (
        calc.margin
        * calc.liktros_lenght
        * calc.liktros_amount
        * calc.liktros_price_one
    )
    if calc.thimble_amount is None:
        calc.thimble_amount = 0
    if calc.thimble_price_one is None:
        calc.thimble_price_one = 0
    calc.thimble_price_total = (
        calc.margin * calc.thimble_amount * calc.thimble_price_one
    )
    if calc.clamp_amount is None:
        calc.clamp_amount = 0
    if calc.clamp_price_one is None:
        calc.clamp_price_one = 0
    calc.clamp_price_total = (
        calc.margin * calc.clamp_amount * calc.clamp_price_one
    )
    if calc.nor_amount is None:
        calc.nor_amount = 0
    if calc.nor_price_one is None:
        calc.nor_price_one = 0
    calc.nor_price_total = calc.margin * calc.nor_amount * calc.nor_price_one
    if calc.braid_thimble is None:
        calc.braid_thimble_price_one = 0
    else:
        braid_thimble_rope = get_object_or_404(Rope, type=calc.braid_thimble)
        calc.braid_thimble_price_one = braid_thimble_rope.price_thimble
    if calc.braid_thimble_amount is None:
        calc.braid_thimble_amount = 0
    calc.braid_thimble_price_total = (
        calc.braid_thimble_amount * calc.braid_thimble_price_one
    )
    if calc.crossing is None:
        calc.crossing_price_one = 0
    else:
        crossing_rope = get_object_or_404(Rope, type=calc.crossing)
        calc.crossing_price_one = crossing_rope.price_crossing
    calc.crossing_amount = calc.longitud_amount * calc.across_amount
    calc.crossing_price_total = calc.crossing_amount * calc.crossing_price_one
    if calc.splice is None:
        calc.splice_price_one = 0
    else:
        splice_rope = get_object_or_404(Rope, type=calc.splice)
        calc.splice_price_one = splice_rope.price_splice
    calc.splice_amount = 1
    calc.splice_price_total = calc.splice_amount * calc.splice_price_one
    if calc.braid_oogen is None:
        calc.braid_oogen_price_one = 0
    else:
        braid_oogen_rope = get_object_or_404(Rope, type=calc.braid_oogen)
        calc.braid_oogen_price_one = braid_oogen_rope.price_oogen
    calc.braid_oogen_amount = (calc.longitud_amount + calc.across_amount) * 2
    calc.braid_oogen_price_total = (
        calc.braid_oogen_amount * calc.braid_oogen_price_one
    )
    calc.price_before_discount = (
        calc.longitud_price_total
        + calc.across_price_total
        + calc.liktros_price_total
        + calc.thimble_price_total
        + calc.clamp_price_total
        + calc.nor_price_total
        + calc.crossing_price_total
        + calc.braid_thimble_price_total
        + calc.splice_price_total
        + calc.braid_oogen_price_total
    )
    if calc.discount is None:
        calc.discount = 0
    calc.price_total = (
        (
            calc.longitud_price_total
            + calc.across_price_total
            + calc.liktros_price_total
            + calc.thimble_price_total
            + calc.clamp_price_total
            + calc.nor_price_total
            + calc.crossing_price_total
            + calc.braid_thimble_price_total
            + calc.splice_price_total
            + calc.braid_oogen_price_total
        )
        * (100 - calc.discount)
        / 100
    )
