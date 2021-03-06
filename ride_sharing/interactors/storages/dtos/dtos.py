from dataclasses import dataclass
from datetime import datetime


@dataclass()
class RideRequestDTO:
    from_place: str
    to_place: str
    travel_datetime: datetime
    number_of_seats_required: int
