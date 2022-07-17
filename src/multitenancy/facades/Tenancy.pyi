from masonite.request.request import Request
from ..models.Tenant import Tenant


class Tenancy:

    def reset_connection() -> None:
        """Resets the connection to the default connection."""
        ...

    def set_connection(tenant: Tenant) -> None:
        """Sets the connection for the tenant."""
        ...

    def get_tenants() -> list[Tenant]:
        """Returns a list of all tenants."""
        ...

    def find_tenant(request: Request) -> Tenant | None:
        """Returns the tenant for the current request."""
        ...

    def delete(tenant: Tenant) -> None:
        """Deletes a tenant."""
        ...

    def create(name: str, domain: str, database: str) -> Tenant:
        """Creates a new tenant."""
        ...

    def get_tenant_by_domain(domain: str) -> Tenant | None:
        """Returns a tenant by domain."""
        ...

    def get_tenant_by_database(database: str) -> Tenant | None:
        """Returns a tenant by database."""
        ...

    def get_tenant_by_id(id: int) -> Tenant | None:
        """Returns a tenant by id."""
        ...