from masonite.request.request import Request
from .models.Tenant import Tenant
from masonite.configuration import config
from masoniteorm.connections import ConnectionResolver


class MultiTenancy:
    def __init__(self, application):
        self.app = application
        self.tenant_configs = config("multitenancy.tenants")

    def get_tenants(self, tenants):
        """Returns a list of all tenants."""
        try:
            if tenants == "default":
                tenants = self.__all()
            else:
                tenants = tenants.split(",")
                tenants = [self.__one(tenant) for tenant in tenants]
            return tenants
        except Exception as e:
            print(e)
        return []

    def __all(self):
        """Returns a list of all tenants."""
        return Tenant.all()

    def __one(self, tenant_name):
        """Returns a tenant by name."""
        tenant = Tenant.where("database", tenant_name).first()
        if not tenant:
            raise Exception(f"Tenant: `{tenant_name}` not found!")
        return tenant

    def set_connection(self, tenant):
        """Sets the connection for the tenant."""
        resolver = ConnectionResolver()
        connections = resolver.get_connection_details().copy()
        new_connections = {}
        for key, value in connections.items():
            if key == "default":
                new_connections[key] = value
            else:
                new_connections[key] = value.copy()
                if connections["default"] == "sqlite":
                    new_connections[key]["database"] = f"{tenant.database}.sqlite3"
                else:
                    new_connections[key]["database"] = tenant.database

        ConnectionResolver().set_connection_details(new_connections)

    def delete(self, tenant):
        """Deletes a tenant."""
        tenant.delete()

    def get_subdomain(self, request: Request):
        """Returns the subdomain for the current request."""
        hosts = [request.environ.get("HTTP_HOST"), request.environ.get("HTTP_X_FORWARDED_HOST")]
        subdomains = []
        for host in hosts:
            if host:
                items = host.split(".")
                if len(items) > 2:
                    subdomains.append(items[0])
        return subdomains, hosts

    def reset_connection(self):
        resolver = ConnectionResolver()
        connections = resolver.get_connection_details()
        database_config = config("database.databases")
        current_db = connections.get(connections.get("default"))["database"]
        original_db = database_config.get(connections.get("default"))["database"]

        if current_db != original_db:
            ConnectionResolver().set_connection_details(database_config)

    def use_tenant(self, tenant):
        """Sets the tenant for the current request."""
        self.reset_connection()
        self.set_connection(tenant)

    def find_tenant(self, request: Request) -> Tenant:
        """Finds the tenant for the current request."""
        subdomains, hosts = self.get_subdomain(request)
        subdomains = tuple(subdomains)
        hosts = tuple(hosts)
        try:
            self.reset_connection()
            return Tenant.where_raw("database in {database}".format(database=subdomains)).first()
        except Exception:
            return None

    def create(self, name: str, database: str, domain: str):
        """Creates a new tenant."""

        tenant = Tenant.where("domain", domain).or_where("database", database).first()
        if tenant:
            raise Exception(
                f"Tenant: Domain: `{domain}` or Database: `{database}` already exists!"
            )

        tenant = Tenant.create(name=name, domain=domain, database=database)
        return tenant

    def get_tenant_by_domain(self, domain: str):
        """Returns a tenant by domain."""

        return Tenant.where("domain", domain).first()

    def get_tenant_by_database(self, database: str):
        """Returns a tenant by database."""

        return Tenant.where("database", database).first()

    def get_tenant_by_id(self, id: int):
        """Returns a tenant by id."""

        return Tenant.find(id)
