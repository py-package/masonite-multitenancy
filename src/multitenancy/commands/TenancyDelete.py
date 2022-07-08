from masonite.commands import Command


class TenancyDelete(Command):
    """
    Delete all tenants or a specific tenant.

    tenancy:delete
        {--tenants=default : List of tenants to delete}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application
        self.tenancy = self.app.make("multitenancy")

    def get_tenants(self):
        """Returns a list of all tenants."""
        tenants = self.option("tenants")
        try:
            if tenants == "default":
                tenants = self.tenancy.get_tenants()
            else:
                tenants = tenants.split(",")
                tenants = [self.tenancy.get_tenant(tenant) for tenant in tenants]
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
            self.app.make("multitenancy").delete(tenant)

        self.info("All tenants deleted!")
