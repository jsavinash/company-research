"""Model routing strategy (small/fast vs frontier)."""
from ..models.enums import ModelTier


class ModelRouter:
    """Routes a task to a model tier based on complexity.

    Simple extraction -> small/fast; complex reasoning -> frontier.
    """

    _FRONTIER_KEYWORDS = ("explain", "scenario", "narrate", "reason", "why")

    def route(self, task: str) -> ModelTier:
        lowered = task.lower()
        if any(k in lowered for k in self._FRONTIER_KEYWORDS):
            return ModelTier.FRONTIER
        return ModelTier.SMALL