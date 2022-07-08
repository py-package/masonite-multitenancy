from masonite.commands import Command
from ..models.Tenant import Tenant


class TenancyList(Command):
    """
    List all tenants.

    tenancy:list
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        tenants = Tenant.all()

        if len(tenants) == 0:
            self.error("No tenants found!")
            exit()

        self.info("=================Tenants List=================")
        for tenant in tenants:
            print("Tenant: " + tenant.name)
            print("Domain: " + tenant.domain)
            print("Database: " + tenant.database)
            print("----------------------------------------------")
