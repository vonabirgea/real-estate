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
    """
    Модель квартиры

    Поля модели:
        number: int - номер квартиры в доме
        area: float - площадь квартиры в квадратных метрах
        rooms_count: int - число комнат в квартире
        wc_count: int - число санузлов в квартире
        floor: Floor - внешний ключ к этажу, накотором расположена квартира
        status: str - статус квартиры (Доступна, Забронирована, Продана)
        description: str - текстовое описание квартиры
    """

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
    """
    Модель этажа

    Поля модели:
        floor: int - этаж
        flats_count: int - число квартир на этаже согласно проекта
        status: str - статус этажа
        description: str - текстовое описание этажа
        entrance: Entrance - внешний ключ к подъезду, в которо расположен этаж
    """

    class StatusChoices(models.TextChoices):
        FREE = "FRE", "Полностью свободен"
        PARTLY = "PRT", "Частично занят"
        SOLD = "SLD", "Полностью выкуплен"

    floor = models.IntegerField(verbose_name="Этаж")
    flats_count = models.IntegerField(
        verbose_name="Число квартир на этаже", null=True
    )
    status = models.CharField(
        max_length=3,
        choices=StatusChoices,
        default=StatusChoices.FREE,
        verbose_name="Статус",
    )
    description = models.TextField(blank=True, verbose_name="Описание этажа")
    entrance = models.ForeignKey(
        to="Entrance",
        verbose_name="Подъезд",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f"Этаж {self.floor} с {self.flats_count} квартирами."

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"


class Entrance(BaseModel):
    """
    Модель подъезда

    Поля модели:
        number: int - номер подъезда в доме
        flats_count: int - число квартир в подъезде согласно проекта
        floors_count: int - число этажей в подъезде согласно проекта
        building: Building - внешний ключ к зданию, в котором расположен подъезд
    """

    number = models.IntegerField(verbose_name="Номер подъезда")
    flats_count = models.IntegerField(verbose_name="Общее число квартир")
    floors_count = models.IntegerField(verbose_name="Общее число этажей")
    building = models.ForeignKey(
        to="Building", verbose_name="Дом", on_delete=models.CASCADE, null=True
    )

    def __str__(self) -> str:
        return f"Подъезд №{self.number}."

    class Meta:
        verbose_name = "Подъезд"
        verbose_name_plural = "Подъезды"


class Building(BaseModel):
    """
    Модель здания

    Поля модели:
        number: int - номер дома
        entrances_count: int - число подъездов в доме согласно проекта
        project: Project - внешний ключ к проекту (ЖК), которому принадлежит дом
        max_floors: int - максимальная этажность дома, согласно проекта
        comissioning_date: date - дата сдачи дома в эксплуатацию согласно проектной документации
        address: str - адрес дома
    """

    number = models.IntegerField(verbose_name="Номер дома (корпуса)")
    entrances_count = models.IntegerField(verbose_name="Число подъездов в доме")
    project = models.ForeignKey(
        "Project", verbose_name="Проект", on_delete=models.CASCADE
    )
    max_floors = models.IntegerField(verbose_name="Этажность", null=True)
    commissioning_date = models.DateField(
        null=True, verbose_name="Дата сдачи дома"
    )
    address = models.CharField(max_length=50, verbose_name="Адрес", null=True)

    def __str__(self) -> str:
        return f"Дом номер {self.number}"

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"


class Project(BaseModel):
    """
    Модель проекта (ЖК)

    Поля модели:
        name: str - название проекта (ЖК)
        buildings_count: int - число домов в проекте согласно проектной документации
        description: str - текстовое описание проекта
        city: str - город, в котором расположен проект (ЖК)
    """

    name = models.CharField(verbose_name="Название проекта", max_length=50)
    buildings_count = models.IntegerField(verbose_name="Число домов в проекте")
    description = models.TextField(max_length=150, verbose_name="Описание")
    city = models.CharField(max_length=20, verbose_name="Город", null=True)

    def __str__(self) -> str:
        return f"Проект {self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
