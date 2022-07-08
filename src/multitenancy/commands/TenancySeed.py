from masonite.commands.Command import Command
from masoniteorm.seeds import Seeder
from inflection import camelize, underscore


class TenancySeed(Command):
    """
    Seed data to all tenants or to a specific tenant.

    tenancy:seed:run
        {--tenants=default : List of tenants to run seeder}
        {--dry : If the seed should run in dry mode}
        {table=None : Name of the table to seed}
        {--d|directory=databases/seeds : The location of the seed directory}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application
        self.tenancy = self.app.make("multitenancy")

    def seed(self, tenant):
        self.tenancy.setup_connection(tenant)

        seeder = Seeder(
            dry=self.option("dry"),
            seed_path=self.option("directory"),
            connection=tenant.database,
        )

        if self.argument("table") == "None":
            seeder.run_database_seed()
            seeder_seeded = "Database Seeder"
        else:
            table = self.argument("table")
            seeder_file = f"{underscore(table)}_table_seeder.{camelize(table)}TableSeeder"
            seeder.run_specific_seed(seeder_file)
            seeder_seeded = f"{camelize(table)}TableSeeder"

        self.line(f"<info>{seeder_seeded} seeded!</info>")

    def handle(self):
        tenants = self.tenancy.get_tenants(self.option("tenants"))

        if len(tenants) == 0:
            self.error("No tenants found!")
            exit()

        for tenant in tenants:
            self.info(f"Seeding tenant: {tenant.name}")
            self.warning("=====================START=====================")
            self.seed(tenant)
            self.warning("======================END======================")
