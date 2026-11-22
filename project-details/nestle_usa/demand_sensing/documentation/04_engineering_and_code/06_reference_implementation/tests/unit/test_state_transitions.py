"""Unit tests for forecast run state transitions."""
import unittest

from src.models.entities import ForecastRun
from src.models.enums import Status


class StateTransitionTest(unittest.TestCase):
    def test_happy_path(self) -> None:
        run = ForecastRun(run_id="r1", model_version="v1")
        self.assertEqual(run.status, Status.QUEUED)
        run.start()
        self.assertEqual(run.status, Status.RUNNING)
        run.complete()
        self.assertEqual(run.status, Status.SUCCEEDED)
        self.assertTrue(run.is_terminal)

    def test_cannot_complete_while_queued(self) -> None:
        run = ForecastRun(run_id="r1", model_version="v1")
        with self.assertRaises(ValueError):
            run.complete()

    def test_cannot_start_twice(self) -> None:
        run = ForecastRun(run_id="r1", model_version="v1")
        run.start()
        with self.assertRaises(ValueError):
            run.start()

    def test_fail_marks_terminal(self) -> None:
        run = ForecastRun(run_id="r1", model_version="v1")
        run.start()
        run.fail("model error")
        self.assertEqual(run.status, Status.FAILED)
        self.assertTrue(run.is_terminal)


if __name__ == "__main__":
    unittest.main()