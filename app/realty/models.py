from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    last_update = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего обновления"
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        get_latest_by = ["-created_at"]


class Flat(BaseModel):
    class StatusChoices(models.TextChoices):
        AVAILABLE = "AVL", "Доступна"
        BOOKED = "BKD", "Забронирована"
        SOLD = "SLD", "Продана"

    class NumOfRoomsChoices(models.IntegerChoices):
        STUDIO = 0, "Студия"
        UNO = 1, "1"
        DOS = 2, "2"
        TRES = 3, "3"
        CUATRO = 4, "4"

    number = models.IntegerField(blank=False, verbose_name="Номер квартиры")
    area = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        verbose_name="Площадь",
    )
    rooms_count = models.IntegerField(
        blank=False, choices=NumOfRoomsChoices, verbose_name="Число комнат"
    )
    wc_count = models.IntegerField(blank=False, verbose_name="Число санузлов")
    floor = models.ForeignKey(
        to="Floor", on_delete=models.CASCADE, null=True, verbose_name="Этаж"
    )
    status = models.CharField(
        max_length=3,
        choices=StatusChoices,
        default=StatusChoices.AVAILABLE,
        verbose_name="Статус",
    )
    description = models.TextField(blank=True, verbose_name="Описание квартиры")

    def __str__(self):
        return f"Квартира №{self.number} площадью {self.area}."

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"


class Floor(BaseModel):
    class StatusChoices(models.TextChoices):
        FREE = "FRE", "Полностью свободен"
        PARTLY = "PRT", "Частично занят"
        SOLD = "SLD", "Полностью выкуплен"

    floor = models.IntegerField(verbose_name="Этаж")
    flats_on_floor = models.IntegerField(
        verbose_name="Количество квартир на этаже"
    )
    status = models.CharField(
        max_length=3,
        choices=StatusChoices,
        default=StatusChoices.FREE,
        verbose_name="Статус",
    )
    description = models.TextField(blank=True, verbose_name="Описание этажа")

    def __str__(self):
        return f"Этаж {self.floor} с {self.flats_on_floor} квартирами."

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"
