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
