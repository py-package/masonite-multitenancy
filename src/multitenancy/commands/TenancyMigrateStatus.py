from masonite.commands.Command import Command
from masoniteorm.migrations import Migration


class TenancyMigrateStatus(Command):
    """
    Display migration status of all tenants or of a specific tenant.

    tenancy:migrate:status
        {--tenants=default : List of tenants}
        {--d|directory=databases/migrations : The location of the migration directory}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application
        self.tenancy = self.app.make("multitenancy")

    def migration(self, tenant):
        self.tenancy.setup_connection(tenant)

        migration = Migration(
            command_class=self,
            connection=tenant.database,
            migration_directory=self.option("directory"),
            config_path=None,
            schema=None,
        )
        migration.create_table_if_not_exists()
        table = self.table()
        table.set_header_row(["Ran?", "Migration"])
        migrations = []

        for migration_file in migration.get_ran_migrations():
            migrations.append(["<info>Y</info>", f"<comment>{migration_file}</comment>"])

        for migration_file in migration.get_unran_migrations():
            migrations.append(["<error>N</error>", f"<comment>{migration_file}</comment>"])

        table.set_rows(migrations)

        table.render(self.io)

    def handle(self):
        tenants = self.tenancy.get_tenants(self.option("tenants"))

        if len(tenants) == 0:
            self.error("No tenants found!")
            exit()

        for tenant in tenants:
            self.info(f"Status of tenant: {tenant.name}")
            self.warning("=====================START=====================")
            self.migration(tenant)
            self.warning("======================END======================")
