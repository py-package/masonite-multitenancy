"""Tenant Model."""
from masoniteorm.models import Model


class Tenant(Model):
    """Tenant Model."""

    __fillable__ = ["name", "domain", "database"]
