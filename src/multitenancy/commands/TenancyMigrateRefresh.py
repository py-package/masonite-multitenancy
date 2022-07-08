from masonite.commands.Command import Command
from masoniteorm.migrations import Migration


class TenancyMigrateRefresh(Command):
    """
    Refreshes database of all tenants or of a specific tenant.

    tenancy:migrate:refresh
        {--tenants=default : List of tenants to migrate}
        {--m|migration=all : Migration's name to be migrated}
        {--d|directory=databases/migrations : The location of the migration directory}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application
        self.tenancy = self.app.make("multitenancy")

    def migration(self, tenant):
        self.tenancy.setup_connection(tenant)

        return Migration(
            command_class=self,
            connection=tenant.database,
            migration_directory=self.option("directory"),
            config_path=None,
            schema=None,
        )

    def handle(self):
        tenants = self.tenancy.get_tenants(self.option("tenants"))

        if len(tenants) == 0:
            self.error("No tenants found!")
            exit()

        for tenant in tenants:
            self.info(f"Refreshing tenant: {tenant.name}")
            self.warning("=====================START=====================")
            self.migration(tenant).refresh(self.option("migration"))
            self.warning("======================END======================")
