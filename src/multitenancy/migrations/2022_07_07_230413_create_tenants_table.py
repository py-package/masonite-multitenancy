"""CreateTenantsTable Migration."""

from masoniteorm.migrations import Migration


class CreateTenantsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("tenants") as table:
            table.increments("id")
            table.string("name")
            table.string("domain").unique()
            table.string("database").unique()
            table.boolean("status").default(False)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("tenants")
