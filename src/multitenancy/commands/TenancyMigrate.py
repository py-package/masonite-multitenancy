import os
from masonite.commands.Command import Command
from masoniteorm.migrations import Migration


class TenancyMigrate(Command):
    """
    Migrates database to all tenants or to a specific tenant.

    tenancy:migrate
        {--tenants=default : List of tenants to migrate}
        {--m|migration=all : Migration's name to be migrated}
        {--f|force : Force migrations without prompt in production}
        {--s|show : Shows the output of SQL for migrations that would be running}
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
        if not migration.get_unran_migrations():
            self.info(f"Nothing to migrate for tenant: {tenant.name}!")
            return

        return migration

    def handle(self):
        if os.getenv("APP_ENV") == "production" and not self.option("force"):
            answer = ""
            while answer not in ["y", "n"]:
                answer = input("Do you want to run migrations in PRODUCTION ? (y/n)\n").lower()
            if answer != "y":
                self.info("Migrations cancelled")
                exit(0)

        tenants = self.tenancy.get_tenants(self.option("tenants"))

        if len(tenants) == 0:
            self.error("No tenants found!")
            exit()

        for tenant in tenants:
            migration = self.migration(tenant)
            if migration:
                migration_name = self.option("migration")
                show_output = self.option("show")
                self.info(f"Migrating tenant: {tenant.name}")
                self.warning("=====================START=====================")
                migration.migrate(migration=migration_name, output=show_output)
                self.warning("======================END======================")
