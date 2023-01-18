from asyncio.windows_events import NULL

from django.db import models


class Rope(models.Model):
    type = models.CharField("Тип каната", max_length=50)
    price = models.FloatField("Цена", blank=True, null=True)
    price_thimble = models.FloatField("Коуш", blank=True, null=True)
    price_oogen = models.FloatField("Огон", blank=True, null=True)
    price_crossing = models.FloatField("Скрещивание", blank=True, null=True)
    price_splice = models.FloatField("Сплесень", blank=True, null=True)

    class Meta:
        verbose_name = "Канат"
        verbose_name_plural = "Канаты"

    def __str__(self):
        return self.type


class CalcPrice(models.Model):
    number = models.IntegerField("Расчет №", blank=True, null=True)
    name_of_rope = models.CharField(
        "Название сети", max_length=150, blank=True
    )
    number_of_check = models.CharField(
        "Номер счета", max_length=50, blank=True
    )
    date_of_check = models.DateField("Дата счета", blank=True, null=True)
    client = models.CharField("Клиент", max_length=150, blank=True, null=True)
    rope_lenght = models.FloatField("Длина, м", blank=True, null=True)
    rope_width = models.FloatField("Ширина, м", blank=True, null=True)
    rope_cell = models.FloatField("Ячейка, мм", blank=True, null=True)
    margin = models.FloatField("Наценка на материалы", blank=True, null=True)
    longitud = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="long",
        blank=True,
        null=True,
        verbose_name="Канат продольный",
    )
    longitud_lenght = models.FloatField("Длина, м", blank=True, null=True)
    longitud_amount = models.FloatField(
        "Количество, шт", blank=True, null=True
    )
    longitud_price_one = models.FloatField(
        "Цена за ед.", blank=True, null=True
    )
    longitud_price_total = models.FloatField(
        "Итого, руб", blank=True, null=True
    )
    across = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="acr",
        blank=True,
        null=True,
        verbose_name="Канат поперечный",
    )
    across_lenght = models.FloatField("Длина, м", blank=True, null=True)
    across_amount = models.FloatField("Количество, шт", blank=True, null=True)
    across_price_one = models.FloatField("Цена за ед.", blank=True, null=True)
    across_price_total = models.FloatField("Итого, руб", blank=True, null=True)
    liktros = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="likt",
        blank=True,
        null=True,
        verbose_name="Ликтрос",
    )
    liktros_lenght = models.FloatField("Длина, м", blank=True, null=True)
    liktros_amount = models.FloatField("Количество, шт", blank=True, null=True)
    liktros_price_one = models.FloatField("Цена за ед.", blank=True, null=True)
    liktros_price_total = models.FloatField(
        "Итого, руб", blank=True, null=True
    )
    thimble_amount = models.FloatField(
        "Коуш, количество, шт", blank=True, null=True
    )
    thimble_price_one = models.FloatField("Цена за ед.", blank=True, null=True)
    thimble_price_total = models.FloatField(
        "Итого, руб", blank=True, null=True
    )
    clamp_amount = models.FloatField(
        "Зажимы, количество, шт", blank=True, null=True
    )
    clamp_price_one = models.FloatField("Цена за ед.", blank=True, null=True)
    clamp_price_total = models.FloatField("Итого, руб", blank=True, null=True)
    nor_amount = models.FloatField(
        "Кольца nor, количество, шт", blank=True, null=True
    )
    nor_price_one = models.FloatField("Цена за ед.", blank=True, null=True)
    nor_price_total = models.FloatField("Итого, руб", blank=True, null=True)
    crossing = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="cros",
        blank=True,
        null=True,
        verbose_name="Скрещивание",
    )
    crossing_amount = models.FloatField(
        "количество, шт", blank=True, null=True
    )
    crossing_price_one = models.FloatField(
        "Цена за ед.", blank=True, null=True
    )
    crossing_price_total = models.FloatField(
        "Итого, руб", blank=True, null=True
    )
    braid_thimble = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="br_th",
        blank=True,
        null=True,
        verbose_name="Заплетка коуша",
    )
    braid_thimble_amount = models.FloatField(
        "количество, шт", blank=True, null=True
    )
    braid_thimble_price_one = models.FloatField(
        "Цена за ед.", blank=True, null=True
    )
    braid_thimble_price_total = models.FloatField(
        "Итого, руб", blank=True, null=True
    )
    splice = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="splice",
        blank=True,
        null=True,
        verbose_name="Сплесень",
    )
    splice_amount = models.FloatField("количество, шт", blank=True, null=True)
    splice_price_one = models.FloatField("Цена за ед.", blank=True, null=True)
    splice_price_total = models.FloatField("Итого, руб", blank=True, null=True)
    braid_oogen = models.ForeignKey(
        Rope,
        on_delete=models.SET_NULL,
        related_name="br_oo",
        blank=True,
        null=True,
        verbose_name="Заплетка огона",
    )
    braid_oogen_amount = models.FloatField(
        "количество, шт", blank=True, null=True
    )
    braid_oogen_price_one = models.FloatField(
        "Цена за ед.", blank=True, null=True
    )
    braid_oogen_price_total = models.FloatField(
        "Итого, руб", blank=True, null=True
    )
    discount = models.IntegerField("Скидка %", blank=True, null=True)
    deadline = models.CharField("Срок выполнения", max_length=50, blank=True)
    comment = models.CharField("Комментарий", max_length=50, blank=True)
    price_before_discount = models.FloatField(
        "Итого по расчету, руб", blank=True, null=True
    )
    price_total = models.FloatField(
        "Итого по счету, руб", blank=True, null=True
    )

    class Meta:
        ordering = ["-number"]
        verbose_name = "Расчет"
        verbose_name_plural = "Расчеты"

    def __str__(self):
        return f"Расчет №{self.number}"
