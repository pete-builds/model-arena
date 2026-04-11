"""Structured exceptions for Open Model Arena."""


class ArenaError(Exception):
    """Base exception for all arena errors."""


class ConfigError(ArenaError):
    """Configuration loading or validation failed."""


class StoreError(ArenaError):
    """Database operation failed."""
