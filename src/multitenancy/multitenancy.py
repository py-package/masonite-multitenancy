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

    def setup_connection(self, tenant):
        self.tenant_configs.update({"default": tenant.database})
        ConnectionResolver().set_connection_details(self.tenant_configs)

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

    def __reset_connection(self):
        ConnectionResolver().set_connection_details(config("database.databases"))

    def find_tenant(self, request: Request):
        """Finds the tenant for the current request."""
        subdomains, hosts = self.get_subdomain(request)
        subdomains = tuple(subdomains)
        hosts = tuple(hosts)
        print(hosts, subdomains)
        try:
            self.__reset_connection()
            tenant = Tenant.where_raw("database in {database}".format(database=subdomains)).first()
            if tenant:
                self.setup_connection(tenant)
                request.tenant = tenant
        except Exception as e:
            print(e)
        return request
