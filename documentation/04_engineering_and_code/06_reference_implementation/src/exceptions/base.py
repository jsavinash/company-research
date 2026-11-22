"""Domain exception hierarchy."""


class DomainError(Exception):
    """Base class for all domain errors."""


class ValidationError(DomainError):
    """Input failed validation."""


class PermissionDeniedError(DomainError):
    """Caller lacks permission for the resource."""


class NotFoundError(DomainError):
    """Requested entity does not exist."""


class ForecastError(DomainError):
    """Base class for forecast failures."""


class InsufficientDataError(ForecastError):
    """Not enough data to produce a confident forecast."""


class ModelDegradedError(ForecastError):
    """Forecast model is degraded; last-good may be served."""


class AttributionError(DomainError):
    """Base class for attribution failures."""


class SignInconsistencyError(AttributionError):
    """Attribution effect sign is inconsistent across windows."""


class UpstreamError(DomainError):
    """A downstream dependency failed."""


class LLMError(UpstreamError):
    """LLM provider error."""


class RateLimitError(UpstreamError):
    """Rate limit exceeded."""


class DataPlatformError(UpstreamError):
    """Snowflake/Databricks error."""


class PolicyViolationError(DomainError):
    """A guardrail / policy was violated."""