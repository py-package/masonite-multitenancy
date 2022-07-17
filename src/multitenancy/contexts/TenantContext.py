# flake8: noqa F501
from typing import Optional
from ..facades import Tenancy
from ..models.Tenant import Tenant
import subprocess
from masonite.environment import env


class TenantContext(object):
    def __init__(self, tenant: Optional[Tenant] = None):
        if not tenant:
            raise Exception("Tenant is required")

        if not isinstance(tenant, Tenant):
            raise Exception("`tenant` must be an instance of Tenant")

        self.tenant = tenant

        self.migration_dir = env("DB_MIGRATIONS_DIR", "databases/migrations")
        self.seeders_dir = env("DB_SEEDERS_DIR", "databases/seeds")

    def __enter__(self):
        Tenancy.set_connection(self.tenant)
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        Tenancy.reset_connection()

    def migrate(self):
        # executes migrations for tenant

        command = f"python craft tenancy:migrate --tenants={self.tenant.database} --d={self.migration_dir}"

        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, shell=True, universal_newlines=True
        )
        output, error = process.communicate()

        if error:
            print(error)
        return output

    def migrate_refresh(self):
        # refreshes database of a tenant

        command = f"python craft tenancy:migrate:refresh --tenants={self.tenant.database} --d={self.migration_dir}"

        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, shell=True, universal_newlines=True
        )
        output, error = process.communicate()

        if error:
            print(error)
        return output

    def migrate_rollback(self):
        # rolls back migration changes in database of a tenant

        command = f"python craft tenancy:migrate:rollback --tenants={self.tenant.database} --d={self.migration_dir}"

        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, shell=True, universal_newlines=True
        )
        output, error = process.communicate()

        if error:
            print(error)
        return output

    def migrate_reset(self):
        # Resets the database of a tenant

        command = f"python craft tenancy:migrate:reset --tenants={self.tenant.database} --d={self.migration_dir}"

        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, shell=True, universal_newlines=True
        )
        output, error = process.communicate()

        if error:
            print(error)
        return output

    def migrate_status(self):
        # displays migration status of a tenant

        command = f"python craft tenancy:migrate:status --tenants={self.tenant.database} --d={self.migration_dir}"

        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, shell=True, universal_newlines=True
        )
        output, error = process.communicate()

        if error:
            print(error)
        return output

    def seed(self):
        # seeds data into database of a tenant

        command = f"python craft tenancy:seed:run --tenants={self.tenant.database} --d={self.seeders_dir}"

        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, shell=True, universal_newlines=True
        )
        output, error = process.communicate()

        if error:
            print(error)
        return output
