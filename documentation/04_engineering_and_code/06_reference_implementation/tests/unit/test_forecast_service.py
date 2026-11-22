"""Unit tests for the forecast service."""
import unittest

from src.exceptions.base import InsufficientDataError
from src.services.forecast_service import ForecastService, StubForecastModel
from src.models.enums import Status


class ForecastServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ForecastService(model=StubForecastModel())

    def test_run_forecast_returns_intervals(self) -> None:
        run = self.service.run_forecast("SKU1", ["S1", "S2"], 12)
        self.assertEqual(run.status, Status.SUCCEEDED)
        self.assertEqual(len(run.lines), 2)
        for line in run.lines:
            self.assertLessEqual(line.interval.p10, line.interval.p50)
            self.assertLessEqual(line.interval.p50, line.interval.p90)

    def test_invalid_horizon_raises(self) -> None:
        with self.assertRaises(InsufficientDataError):
            self.service.run_forecast("SKU1", ["S1"], 0)

    def test_run_id_is_unique(self) -> None:
        r1 = self.service.run_forecast("SKU1", ["S1"], 4)
        r2 = self.service.run_forecast("SKU1", ["S1"], 4)
        self.assertNotEqual(r1.run_id, r2.run_id)


if __name__ == "__main__":
    unittest.main()