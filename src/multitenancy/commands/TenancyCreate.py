from masonite.commands import Command
from ..models.Tenant import Tenant


class TenancyCreate(Command):
    """
    Creates a new tenant.

    tenancy:create
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        name = self.ask("Name: ")
        domain = self.ask("Domain: ")
        database = self.ask("Database: ")

        if not name:
            self.error("Name is required!")
            exit()

        if not domain:
            self.error("Domain is required!")
            exit()

        if not database:
            self.error("Database name is required!")
            exit()

        tenant = Tenant.where("domain", domain).or_where("database", database).first()
        if tenant:
            self.error("Tenant already exists!")
            exit()

        tenant = Tenant.create(name=name, domain=domain, database=database)
        self.info("Tenant created!")
