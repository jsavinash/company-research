"""Attribution strategies (Strategy pattern).

Swappable causal methods behind a common interface.
"""
from typing import Protocol

from ..models.enums import Driver
from ..models.value_objects import DriverEffect


class AttributionStrategy(Protocol):
    def attribute(self, delta: float, drivers: list[Driver]) -> list[DriverEffect]:
        ...


class SyntheticControlAttribution:
    """Synthetic control / DiD-style attribution.

    Deterministic stub for the reference implementation: distributes the
    delta across drivers with fixed weights and a confidence score.
    """

    _WEIGHTS = {
        Driver.GLP1: 0.45,
        Driver.PRICE: 0.25,
        Driver.DISTRIBUTION: 0.18,
        Driver.PRIVATE_LABEL: 0.12,
    }

    def attribute(self, delta: float, drivers: list[Driver]) -> list[DriverEffect]:
        total = sum(self._WEIGHTS.get(d, 0.0) for d in drivers) or 1.0
        return [
            DriverEffect(
                driver=d,
                effect=delta * self._WEIGHTS.get(d, 0.0) / total,
                confidence=0.8,
            )
            for d in drivers
        ]


class DiffInDiffAttribution:
    """Difference-in-differences attribution (stub)."""

    def attribute(self, delta: float, drivers: list[Driver]) -> list[DriverEffect]:
        n = len(drivers) or 1
        return [
            DriverEffect(driver=d, effect=delta / n, confidence=0.7)
            for d in drivers
        ]