from masonite.commands.Command import Command
from masoniteorm.migrations import Migration


class TenancyMigrateReset(Command):
    """
    Resets migration of all tenants or of a specific tenant.

    tenancy:migrate:reset
        {--tenants=default : List of tenants to reset}
        {--m|migration=all : Migration's name to reset}
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
            self.info(f"Resetting tenant: {tenant.name}")
            self.warning("=====================START=====================")
            self.migration(tenant).reset(self.option("migration"))
            self.warning("======================END======================")
