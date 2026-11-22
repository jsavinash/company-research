"""Domain entities."""
from dataclasses import dataclass, field
from datetime import datetime, timezone

from .enums import Driver, Status
from .value_objects import Interval


@dataclass
class ForecastLine:
    sku_id: str
    store_id: str
    week: str
    interval: Interval


@dataclass
class Attribution:
    driver: Driver
    effect: float
    confidence: float


@dataclass
class ForecastRun:
    run_id: str
    model_version: str
    lines: list[ForecastLine] = field(default_factory=list)
    attributions: list[Attribution] = field(default_factory=list)
    status: Status = Status.QUEUED
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def start(self) -> None:
        if self.status is not Status.QUEUED:
            raise ValueError(f"cannot start run in status {self.status}")
        self.status = Status.RUNNING

    def complete(self) -> None:
        if self.status is not Status.RUNNING:
            raise ValueError(f"cannot complete run in status {self.status}")
        self.status = Status.SUCCEEDED

    def fail(self, reason: str = "") -> None:
        self.status = Status.FAILED
        self._failure_reason = reason

    @property
    def is_terminal(self) -> bool:
        return self.status in (Status.SUCCEEDED, Status.FAILED)