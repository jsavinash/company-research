"""Forecast service with per-(sku, store) locking."""
import threading
import uuid
from contextlib import contextmanager

from ..exceptions.base import InsufficientDataError
from ..models.entities import ForecastLine, ForecastRun
from ..models.enums import Driver, Status
from ..models.value_objects import Interval


class _LockRegistry:
    """Process-local lock registry keyed by (sku_id, store_id)."""

    def __init__(self) -> None:
        self._locks: dict[tuple[str, str], threading.Lock] = {}
        self._guard = threading.Lock()

    @contextmanager
    def lock(self, key: tuple[str, str]):
        with self._guard:
            lock = self._locks.setdefault(key, threading.Lock())
        with lock:
            yield


class StubForecastModel:
    """Deterministic stand-in for a LightGBM/TFT model."""

    version = "stub-1.0"

    def predict(self, sku_id: str, store_ids: list[str], horizon_weeks: int) -> list[ForecastLine]:
        lines = []
        for store in store_ids:
            base = 100.0 + (hash((sku_id, store)) % 50)
            interval = Interval(p10=base * 0.9, p50=base, p90=base * 1.1)
            lines.append(ForecastLine(sku_id=sku_id, store_id=store, week=f"horizon-{horizon_weeks}", interval=interval))
        return lines


class ForecastService:
    def __init__(self, model=None, locks: _LockRegistry | None = None) -> None:
        self.model = model or StubForecastModel()
        self._locks = locks or _LockRegistry()

    def run_forecast(
        self,
        sku_id: str,
        store_ids: list[str],
        horizon_weeks: int,
    ) -> ForecastRun:
        if horizon_weeks <= 0:
            raise InsufficientDataError("horizon_weeks must be positive")
        run = ForecastRun(run_id=str(uuid.uuid4()), model_version=self.model.version)
        run.start()
        for store in store_ids:
            with self._locks.lock((sku_id, store)):
                lines = self.model.predict(sku_id, [store], horizon_weeks)
                run.lines.extend(lines)
        run.complete()
        return run