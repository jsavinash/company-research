"""Attribution service (Strategy pattern in action)."""
from ..models.enums import Driver
from ..models.value_objects import DriverEffect
from ..strategies.attribution_strategy import AttributionStrategy, SyntheticControlAttribution


class AttributionService:
    def __init__(self, strategy: AttributionStrategy | None = None) -> None:
        self.strategy = strategy or SyntheticControlAttribution()

    def attribute(self, delta: float, drivers: list[Driver]) -> list[DriverEffect]:
        return self.strategy.attribute(delta, drivers)