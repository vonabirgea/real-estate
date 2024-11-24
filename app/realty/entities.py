from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class FlatEntity:
    id: int
    number: int
    area: float
    rooms_count: int
    wc_count: int
    floor_id: int
    status: str
    description: str
    created_at: datetime
    last_update: datetime


@dataclass
class FloorEntity:
    id: int
    storey: int
    flats_count: int
    status: str
    description: str
    entrance_id: int
    created_at: datetime
    last_update: datetime


@dataclass
class EntranceEntity:
    id: int
    number: int
    flats_count: int
    floors_count: int
    building_id: int
    created_at: datetime
    last_update: datetime


@dataclass
class BuildingEntity:
    id: int
    number: int
    entrances_count: int
    project_id: int
    max_floors: int
    commissioning_date: date
    address: str
    created_at: datetime
    last_update: datetime


@dataclass
class ProjectEntity:
    id: int
    name: str
    buildings_count: int
    description: str
    city: str
    created_at: datetime
    last_update: datetime
