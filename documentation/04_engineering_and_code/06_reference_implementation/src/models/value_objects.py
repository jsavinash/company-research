"""Value objects: immutable, self-validating domain primitives."""
from dataclasses import dataclass

from .enums import Driver


@dataclass(frozen=True)
class Interval:
    """A calibrated prediction interval. Invariant: p10 <= p50 <= p90."""
    p10: float
    p50: float
    p90: float

    def __post_init__(self) -> None:
        if not (self.p10 <= self.p50 <= self.p90):
            raise ValueError(
                f"invalid interval: p10={self.p10} <= p50={self.p50} <= p90={self.p90}"
            )


@dataclass(frozen=True)
class DriverEffect:
    """A single causal attribution result."""
    driver: Driver
    effect: float
    confidence: float

    def __post_init__(self) -> None:
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"confidence must be in [0,1], got {self.confidence}")