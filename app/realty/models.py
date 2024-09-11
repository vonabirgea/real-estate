from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        get_latest_by = ["-created_at"]


class Flat(BaseModel):
    class StatusChoices(models.TextChoices):
        AVAILABLE = "AVL", "Доступна"
        BOOKED = "BKD", "Забронирована"
        SOLD = "SLD", "Продана"

    class NumOfRoomsChoices(models.TextChoices):
        STUDIO = "STU", "Студия"
        UNO = "1", "1"
        DOS = "2", "2"
        TRES = "3", "3"
        CUATRO = "4", "4"

    area = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False, verbose_name="Площадь"
    )
    num_of_rooms = models.CharField(
        max_length=3, choices=NumOfRoomsChoices, verbose_name="Число комнат"
    )
    num_of_wc = models.IntegerField(blank=False, verbose_name="Число санузлов")
    floor = models.IntegerField(blank=False, verbose_name="Этаж")
    status = models.CharField(
        max_length=3,
        choices=StatusChoices,
        default=StatusChoices.AVAILABLE,
        verbose_name="Статус",
    )

    def __str__(self):
        return f"Квартира №{self.pk} площадью {self.area} на {self.floor} этаже."

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
