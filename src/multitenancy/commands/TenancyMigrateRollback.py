from masonite.commands.Command import Command
from masoniteorm.migrations import Migration


class TenancyMigrateRollback(Command):
    """
    Rolls back the last batch of migration of all tenants or of a specific tenant.

    tenancy:migrate:rollback
        {--tenants=default : List of tenants to reset}
        {--m|migration=all : Migration's name to reset}
        {--s|show : Shows the output of SQL for migrations that would be running}
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
            self.info(f"Rolling back tenant: {tenant.name}")
            self.warning("=====================START=====================")
            self.migration(tenant).rollback(
                migration=self.option("migration"), output=self.option("show")
            )
            self.warning("======================END======================")
