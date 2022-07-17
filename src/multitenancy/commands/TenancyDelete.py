from masonite.commands import Command
from ..facades import Tenancy


class TenancyDelete(Command):
    """
    Delete all tenants or a specific tenant.

    tenancy:delete
        {--tenants=default : List of tenants to delete}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def get_tenants(self):
        """Returns a list of all tenants."""
        tenants = self.option("tenants")
        try:
            if tenants == "default":
                tenants = Tenancy.get_tenants()
            else:
                tenants = tenants.split(",")
                tenants = [Tenancy.get_tenant(tenant) for tenant in tenants]
            return tenants
        except Exception as e:
            self.error(e)
        return []

    def handle(self):
        tenants = self.get_tenants()

        if len(tenants) == 0:
            self.error("No tenants found!")
            exit()

        for tenant in tenants:
            Tenancy.delete(tenant)

        self.info("All tenants deleted!")
