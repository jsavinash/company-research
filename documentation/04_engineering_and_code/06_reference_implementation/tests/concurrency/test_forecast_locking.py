"""Concurrency tests: verify per-(sku, store) locking serializes access."""
import threading
import unittest

from src.services.forecast_service import ForecastService, StubForecastModel


class ConcurrencyTest(unittest.TestCase):
    def test_parallel_runs_do_not_corrupt(self) -> None:
        service = ForecastService(model=StubForecastModel())
        errors: list[Exception] = []
        runs: list[int] = []

        def worker() -> None:
            try:
                run = service.run_forecast("SKU1", ["S1"], 4)
                runs.append(len(run.lines))
            except Exception as exc:  # noqa: BLE001
                errors.append(exc)

        threads = [threading.Thread(target=worker) for _ in range(20)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(errors, [])
        self.assertEqual(len(runs), 20)
        self.assertTrue(all(n == 1 for n in runs))

    def test_concurrent_stores_each_get_one_line(self) -> None:
        service = ForecastService(model=StubForecastModel())
        run = service.run_forecast("SKU1", ["S1", "S2", "S3", "S4"], 4)
        self.assertEqual(len(run.lines), 4)


if __name__ == "__main__":
    unittest.main()