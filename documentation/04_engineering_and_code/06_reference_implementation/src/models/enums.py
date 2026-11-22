"""Domain enums for the Demand Sensing reference implementation."""
from enum import Enum


class Status(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class Driver(str, Enum):
    GLP1 = "glp1"
    PRICE = "price"
    MIX = "mix"
    DISTRIBUTION = "distribution"
    PRIVATE_LABEL = "private_label"


class ModelTier(str, Enum):
    SMALL = "small"
    FRONTIER = "frontier"